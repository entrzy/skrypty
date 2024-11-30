import requests
from bs4 import BeautifulSoup
import time

# Funkcja, która pobiera i parsuje stronę dla pojedynczej drużyny
def get_match_results(team_name, url):
    time.sleep(2)
    response = requests.get(url)
    
    # Sprawdzenie, czy strona została poprawnie załadowana
    if response.status_code != 200:
        print(f"Błąd: Nie można załadować strony dla {team_name}. Status: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Znajdź wszystkie <div> z klasą "gres", które zawierają wyniki meczów
    result_divs = soup.find_all('div', class_='gres')
    
    # Zmienna do przechowywania rezultatów (W, D, L)
    results = []

    # Iteracja po znalezionych divach
    for result_div in result_divs:
        result = result_div.text.strip()  # Pobierz tekst i usuń białe znaki
        
        # Dopasowanie wyniku do odpowiednich liter
        if result == 'W':
            results.append('W')
        elif result == 'L':
            results.append('L')
        elif result == 'D':
            results.append('D')
        else:
            # Pomijamy inne symbole
            continue

    # Połącz wyniki w jeden ciąg znaków
    return team_name, ''.join(results)


# Funkcja, która pobiera drużyny z danej ligi
def get_teams_from_league(url):
    time.sleep(2)
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Błąd: Nie można załadować strony dla {url}. Status: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Znalezienie div z klasą template_table i id league-table
    league_table_div = soup.find('div', class_='template_table', id='league-table')
    
    if league_table_div is None:
        print(f"Błąd: Nie znaleziono tabeli ligowej dla {url}.")
        return []
    
    # Wyszukiwanie linków zaczynających się na "/teams/" tylko w obrębie tego diva
    team_links = league_table_div.find_all('a', href=lambda href: href and href.startswith('/teams/'))
    
    # Lista URL-i i nazw drużyn
    teams = [(link.text.strip(), "https://pl.fctables.com" + link['href']) for link in team_links]
    
    return team


# Lista lig, które chcemy przetworzyć
leagues = [
    ("Polska", "https://pl.fctables.com/polska/ekstraklasa/"),
    ("Anglia", "https://pl.fctables.com/anglia/premier-league/"),
    ("Hiszpania", "https://pl.fctables.com/hiszpania/primera-division/"),
    ("Niemcy", "https://pl.fctables.com/niemcy/bundesliga/"),
    ("Włochy", "https://pl.fctables.com/wlochy/serie-a/"),
    ("Francja", "https://pl.fctables.com/francja/ligue-1/"),
    # Możesz dodać więcej lig tutaj, np. Bundesliga, La Liga itp.
]

# Pętla do pobierania drużyn i wyników dla każdej ligi
for league_name, league_url in leagues:
    print(f"\nLiga: {league_name}")
    
    # Pobierz drużyny z danej ligi
    teams = get_teams_from_league(league_url)
    
    if not teams:
        print(f"Brak drużyn do wyświetlenia dla ligi {league_name}.")
        continue

    
    # Pętla do pobierania wyników dla każdej drużyny
    for team_name, url in teams:
        team_results = get_match_results(team_name, url)
        
        if team_results:
            name, results = team_results
            # Sprawdź, czy drużyna nie ma remisu ("D") w wynikach
            if 'D' not in results:
                print(f"{name}:")

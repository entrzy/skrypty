./ssoadm create-site -u amAdmin -f /path/to/passwordfile.txt -e /site-id -s http://site-url:port -t primary
./ssoadm add-site-members -u amAdmin -f /path/to/passwordfile.txt -e /site-id -m server01,server02
./ssoadm list-sites -u amAdmin -f /path/to/passwordfile.txt






#!/bin/bash

# Funkcja do wyszukiwania i zamiany plików
search_and_replace() {
    local search_path=$1
    local search_term=$2
    local replace_term=$3
    
    # Wyszukaj pliki zawierające określony ciąg znaków
    files=$(grep -l -r "$search_term" "$search_path")

    # Jeśli nie znaleziono plików, wyświetl komunikat
    if [ -z "$files" ]; then
        echo "Nie znaleziono plików zawierających \"$search_term\" w ścieżce \"$search_path\"."
        return
    fi

    # Wyświetl znalezione pliki
    echo "Znalezione pliki zawierające \"$search_term\" w ścieżce \"$search_path\":"
    echo "$files"

    # Potwierdzenie od użytkownika
    read -p "Czy chcesz zamienić \"$search_term\" na \"$replace_term\" w tych plikach? (t/n): " confirm
    if [ "$confirm" != "t" ]; then
        echo "Operacja anulowana."
        return
    fi

    # Zamień ciąg znaków w plikach
    for file in $files; do
        sed -i "s/$search_term/$replace_term/g" "$file"
        echo "Zamieniono \"$search_term\" na \"$replace_term\" w pliku $file."
    done

    echo "Zakończono zamianę."
}

# Sprawdź, czy podano poprawną liczbę argumentów
if [ "$#" -ne 3 ]; then
    echo "Sposób użycia: $0 ścieżka_do_katalogu_ciąg_znaków_do_wyszukania ciąg_znaków_do_zamiany"
    exit 1
fi

# Pobierz od użytkownika ścieżkę, ciągi znaków do wyszukania i zamiany
search_path=$1
search_term=$2
replace_term=$3

# Wywołaj funkcję wyszukiwania i zamiany
search_and_replace "$search_path" "$search_term" "$replace_term"

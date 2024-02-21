# Definiowanie ścieżki do katalogu, który ma być przeszukany
$folderPath = "C:\Sciezka\Do\Katalogu"

# Definiowanie tekstu, który ma być wyszukiwany w plikach
$searchText = "TekstDoWyszukania"

# Pobieranie listy plików w katalogu
$files = Get-ChildItem -Path $folderPath -Recurse -File

# Przeszukiwanie każdego pliku w poszukiwaniu tekstu
foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    if ($content -match $searchText) {
        Write-Output "Znaleziono tekst '$searchText' w pliku: $($file.FullName)"
    }
}

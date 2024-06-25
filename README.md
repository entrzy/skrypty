# Ścieżka do pliku .p12
$certPath = "C:\sciezka\do\certyfikatu\certyfikat.p12"

# Hasło do pliku .p12 (jeśli jest wymagane)
$certPassword = "TwojeHaslo"

# Importowanie certyfikatu z pliku .p12
$cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2
$cert.Import($certPath, $certPassword, [System.Security.Cryptography.X509Certificates.X509KeyStorageFlags]::PersistKeySet)

# Wyświetlanie daty ważności certyfikatu
"NotBefore: " + $cert.NotBefore
"NotAfter: " + $cert.NotAfter

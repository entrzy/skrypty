
Aby zaimportować certyfikat z rozszerzeniem .cer do serwera Tomcat 9 na systemie Linux, musisz przekonwertować ten certyfikat do formatu używanego przez Tomcat, czyli do pliku keystore Java (JKS lub PKCS12). Oto kroki, które należy wykonać:

1. Instalacja narzędzia keytool
Upewnij się, że masz zainstalowane narzędzie keytool, które jest częścią Java Development Kit (JDK). Możesz to sprawdzić, wpisując w terminalu:

bash
Copy code
keytool -help
Jeśli narzędzie nie jest zainstalowane, zainstaluj JDK zgodnie z dystrybucją Linuxa, którą posiadasz.

2. Konwersja pliku .cer do keystore
Najpierw, jeśli masz tylko publiczny certyfikat (plik .cer), musisz mieć także klucz prywatny, z którym certyfikat ten został wydany. Zakładając, że masz klucz prywatny oraz certyfikat, możesz utworzyć plik keystore w formacie PKCS12, który jest obecnie preferowany przez Tomcat:

bash
Copy code
openssl pkcs12 -export -in mycert.cer -inkey mykey.key -out keystore.p12 -name alias_name
W powyższym poleceniu:

mycert.cer to twój certyfikat.
mykey.key to twój klucz prywatny.
keystore.p12 to nazwa pliku keystore, który zostanie utworzony.
alias_name to alias, pod którym klucz prywatny i certyfikat będą przechowywane w keystore.
3. Konfiguracja Tomcata do używania nowego keystore
Edytuj plik konfiguracyjny Tomcata server.xml, który znajdziesz w katalogu conf w katalogu instalacyjnym Tomcata. Znajdź definicję konektora dla HTTPS, która wygląda mniej więcej tak:

xml
Copy code
<Connector port="8443" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="8443"
           scheme="https"
           secure="true"
           SSLEnabled="true"
           keystoreFile="/path/to/keystore.p12"
           keystorePass="password"
           keystoreType="PKCS12" />
W powyższym przykładzie:

keystoreFile wskazuje ścieżkę do pliku keystore.
keystorePass to hasło do keystore, które ustawiłeś podczas eksportu do PKCS12.
keystoreType ustawione na PKCS12.
4. Restart Tomcata
Po dokonaniu zmian w konfiguracji, zrestartuj serwer Tomcat, aby zmiany weszły w życie:

bash
Copy code
sudo systemctl restart tomcat9
lub

bash
Copy code
/path/to/tomcat/bin/shutdown.sh
/path/to/tomcat/bin/startup.sh
Te kroki powinny pozwolić na skuteczne zaimportowanie i wykorzystanie certyfikatu .cer w Twoim serwerze Tomcat.

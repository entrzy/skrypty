<Connector port="8443" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="8443"
           scheme="https"
           secure="true"
           SSLEnabled="true"
           keystoreFile="/path/to/keystore.p12"
           keystorePass="password"
           keystoreType="PKCS12" />

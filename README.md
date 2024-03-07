ldapmodify -h hostname -p port -D "cn=Directory Manager" -w password -c -a -f new_data.ldif


ldapdelete -h hostname -p port -D "cn=Directory Manager" -w password -r "baseDN"

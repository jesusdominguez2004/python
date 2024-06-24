# W3Schools, Python MySQL, Get Started
import mysql.connector
import mysql_credentials as msqlc

mydb = mysql.connector.connect(
    host = msqlc.host,
    user = msqlc.username,
    password = msqlc.password
)

print(mydb)

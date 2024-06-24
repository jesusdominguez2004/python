# W3Schools, Python MySQL, Create Table
import mysql.connector
import mysql_credentials as mysqlc

mydb = mysql.connector.connect(
    host = mysqlc.host,
    user = mysqlc.username,
    password = mysqlc.password,
    database = "mydatabase",
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

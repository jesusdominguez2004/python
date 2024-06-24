# W3Schools, Python MySQL, Limit
import mysql.connector
import mysql_credentials as mysqlc

mydb = mysql.connector.connect(
    host = mysqlc.host,
    user = mysqlc.username,
    password = mysqlc.password,
    database = "mydatabase",
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

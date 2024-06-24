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

# Start from position 3, and return 5 records
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

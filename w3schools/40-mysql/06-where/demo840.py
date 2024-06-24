# W3Schools, Python MySQL, Where
import mysql.connector
import mysql_credentials as mysqlc

mydb = mysql.connector.connect(
    host = mysqlc.host,
    user = mysqlc.username,
    password = mysqlc.password,
    database = "mydatabase",
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ('Yellow Garden 2', )
mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

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

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# W3Schools, Python MySQL, Join
import mysql.connector
import mysql_credentials as mysqlc

mydb = mysql.connector.connect(
    host = mysqlc.host,
    user = mysqlc.username,
    password = mysqlc.password,
    database = "mydatabase",
)

mycursor = mydb.cursor()

# 1. Insert data to products table
sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
val = [
    (154, 'Chocolate Heaven'),
    (155, 'Tasty Lemons'),
    (156, 'Vanilla Dreams')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# 2. Show data from products table
mycursor.execute("SELECT * FROM products")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

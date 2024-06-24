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

# 1. Insert data to users table
sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
val = [
    ('John', 154),
    ('Peter', 154),
    ('Amy', 155),
    ('Hannah', 0),
    ('Michael', 0)
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# 2. Show data from users table
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

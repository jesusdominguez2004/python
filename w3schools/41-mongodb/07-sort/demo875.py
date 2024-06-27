# W3Schools, Python MongoDB, Sort
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

# Sort the result alphabetically by name:
mydoc = mycol.find().sort("name")

for x in mydoc:
    print(x)

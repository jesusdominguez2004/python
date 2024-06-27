# W3Schools, Python MongoDB, Sort
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

# Sort the result reverse alphabetically by name:
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
    print(x)

# W3Schools, Python MongoDB, Query
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

# Find documents where the address starts with the letter "S":
myquery = {"address": {"$regex": "^S"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

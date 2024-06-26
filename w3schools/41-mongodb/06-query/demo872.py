# W3Schools, Python MongoDB, Query
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

myquery = {"address": "Park Lane 38"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

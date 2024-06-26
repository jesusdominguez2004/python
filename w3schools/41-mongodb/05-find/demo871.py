# W3Schools, Python MongoDB, Find
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

# This example will exclude "address" from the result:
for x in mycol.find({}, {"address": 0}):
    print(x)

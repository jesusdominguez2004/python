# W3Schools, Python MongoDB, Update
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

# Change the address from "Valley 345" to "Canyon 123":
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)

# print "customers" after the update:
for x in mycol.find():
    print(x)

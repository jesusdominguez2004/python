# W3Schools, Python MongoDB, Delete
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

myquery = { "address": "Mountain 21"}

# Delete the document with the address "Mountain 21":
mycol.delete_one(myquery)

# print the customers collection after the deletion:
for x in mycol.find():
    print(x)

# W3Schools, Python MongoDB, Delete
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

myquery = { "address": {"$regex": "^S"} }

# Delete all documents were the address starts with the letter S:
mycol.delete_many(myquery)

# print the customers collection after the deletion:
for x in mycol.find():
    print(x)

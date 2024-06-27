# W3Schools, Python MongoDB, Update
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

# Update all documents where the address starts with the letter "S":
myquery = { "address": { "$regex": "^S"} }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")

# print "customers" after the update:
for x in mycol.find():
    print(x)

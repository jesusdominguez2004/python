# W3Schools, Python MongoDB, Find
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

# Return only the names and addresses, not the _ids:
for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)

# W3Schools, Python MongoDB, Find
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

# Return all documents 
# in the "customers" collection,
# and print each document:
for x in mycol.find():
    print(x)

# W3Schools, Python MongoDB, Delete
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

# Delete all documents in the "customers" collection:
x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")

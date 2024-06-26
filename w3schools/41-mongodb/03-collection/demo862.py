# W3Schools, Python MongoDB, Collection
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)

mydb = myclient['mydatabase']

mycol = mydb["customers"]

print(mydb.list_collection_names())

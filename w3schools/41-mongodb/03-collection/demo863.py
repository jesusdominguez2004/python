# W3Schools, Python MongoDB, Collection
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)

mydb = myclient['mydatabase']

collist = mydb.list_collection_names()

if "customers" in collist:
    print("The collection exists!")
else:
    print("The collection doesn't exist...")

# W3Schools, Python MongoDB, Create DB
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists!")
else:
    print("The database doesn't exists...")

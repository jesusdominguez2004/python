# W3Schools, Python MongoDB, Create DB
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)

print(myclient.list_database_names())

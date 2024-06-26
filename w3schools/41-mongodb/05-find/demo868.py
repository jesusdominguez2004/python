# W3Schools, Python MongoDB, Find
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

# find the first document in the customers collection
x = mycol.find_one()

print(x)

# W3Schools, Python MongoDB, Limit
import pymongo
import mongodb_credentials as mdbc

myclient = pymongo.MongoClient(mdbc.connection_string)
mydb = myclient['mydatabase']
mycol = mydb["customers"]

# Limit the result to only return 5 documents:
myresult = mycol.find().limit(5)

# print the result:
for x in myresult:
    print(x)

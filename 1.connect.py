# Step 1. Open powershell then run command mongod and then open second powershell run mongo command.
# Step 2. Open MongoDBCompass.

import pymongo

if __name__ == '__main__':
    print("Welcome to Pymongo")

    # connection with local database
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # connection with remote database with access only for 6 hours
    # client = pymongo.MongoClient("mongodb+srv://arpan12:arpan@cluster0.nlazd.mongodb.net/test")

    print(client)
    
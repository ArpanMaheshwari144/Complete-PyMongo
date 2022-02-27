import pymongo

if __name__ == '__main__':
    print("Welcome to Pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['arpan'] # create database if not present and if present so use that database
    collection = db['mySampleCollectionForArpan'] # create collection

    # Using update_one function
    # myprev = {"Name":"Verma"}
    # mynext = {"$set":{"Location":"Mumbai"}}
    # collection.update_one(myprev, mynext)

    # Using update_many function
    myprev = {"Name":"Verma"}
    mynext = {"$set":{"Location":"Mumbai"}}
    mycount = collection.update_many(myprev, mynext)
    print(mycount.modified_count)
    
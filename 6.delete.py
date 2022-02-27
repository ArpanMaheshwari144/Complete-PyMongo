import pymongo

if __name__ == '__main__':
    print("Welcome to Pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['arpan'] # create database if not present and if present so use that database
    collection = db['mySampleCollectionForArpan'] # create collection

    # Using delete_one function
    # rec = {"Name":"Verma"}
    # collection.delete_one(rec)

    # Using delete_one function
    rec = {"Name":"Aditya"}
    mycount = collection.delete_many(rec)
    print(mycount.deleted_count)
    
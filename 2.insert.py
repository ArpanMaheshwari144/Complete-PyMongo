# Open MongoDB Compass then run this file.

import pymongo

if __name__ == '__main__':
    print("Welcome to Pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['arpan'] # create database if not present and if present so use that database
    collection = db['mySampleCollectionForArpan'] # create collection

    # insert data to database by the help of insert_one function
    # dictionary = {'name':'Arpan', 'marks':50}
    # collection.insert_one(dictionary)
    # dictionary2 = {'name':'Arpan2', 'marks':60}
    # collection.insert_one(dictionary2)

    # insert data to database by the help of insert_many function
    insertThese = [
        # {'Name':'Arpan', 'Location':'Punjab', 'Marks':50},
        # {'Name':'Adarsh', 'Location':'Lucknow', 'Marks':60},
        # {'Name':'Aditya', 'Location':'Chennai', 'Marks':45},
        # {'Name':'Verma', 'Location':'Kolkata', 'Marks':55}

        {'_id':1, 'Name':'Arpan', 'Location':'Punjab', 'Marks':50},
        {'_id':2, 'Name':'Adarsh', 'Location':'Lucknow', 'Marks':60},
        {'_id':3, 'Name':'Aditya', 'Location':'Chennai', 'Marks':45},
        {'_id':4, 'Name':'Verma', 'Location':'Kolkata', 'Marks':55}
    ]
    collection.insert_many(insertThese)
    
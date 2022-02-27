import pymongo

if __name__ == '__main__':
    print("Welcome to Pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)

    # print all databases
    allDatabases = client.list_database_names()
    print(allDatabases)

    # print all the collections which are stored in the databases
    myCollection = client['arpan']
    print(myCollection.list_collection_names())
    
import pymongo

if __name__ == '__main__':
    print("Welcome to Pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['arpan'] # create database if not present and if present so use that database
    collection = db['mySampleCollectionForArpan'] # create collection

    # one = collection.find_one()
    # print(one)

    # one = collection.find_one({'Name':'Adarsh'})
    # print(one)

    # allDocs = collection.find({'Name':'Verma'})
    # for item in allDocs:
    #     print(item)

    # allDocs = collection.find({'Name':'Verma'}, {'Name':1})
    # for item in allDocs:
    #     print(item)

    # allDocs = collection.find({'Name':'Verma'}, {'Name':0})
    # for item in allDocs:
    #     print(item)

    # _id is by default print bcoz it's value is _id -> 1, so we explicitly do _id -> 0 so it will not print 
    # allDocs = collection.find({'Name':'Verma'}, {'Name':1, '_id':0})
    # for item in allDocs:
    #     print(item)

    # allDocs = collection.find({'Name':'Verma'}, {'Name':0, '_id':0})
    # for item in allDocs:
    #     print(item)

    # allDocs = collection.find({'Name':'Verma'}, {'Name':0})
    # # print(allDocs.count())
    #     # OR
    # # print(collection.count_documents({}))
    # for item in allDocs:
    #     print(item)

    # limit returns the object
    # allDocs = collection.find({'Name':'Verma'}, {'Name':0}).limit(1)
    # # print(allDocs.count())
    #     # OR
    # # print(collection.count_documents({}))
    # for item in allDocs:
    #     print(item)

    # lte -> less than or equal to
    # allDocs = collection.find({'Name':'Arpan', 'Marks':{'$lte':80}})
    # # print(allDocs.count())
    #     # OR
    # # print(collection.count_documents({}))
    # for item in allDocs:
    #     print(item)

    # gte -> greater than or equal to
    allDocs = collection.find({'Name':'Arpan', 'Marks':{'$gte':80}})
    # print(allDocs.count())
        # OR
    # print(collection.count_documents({}))
    for item in allDocs:
        print(item)
    
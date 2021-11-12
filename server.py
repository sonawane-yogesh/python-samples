def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://localhost:28000/fkreqpkgdb"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['fkreqpkgdb']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    dbName = get_database()


def get_projects():
    # from pymongo_test_insert import get_database
    dbName = get_database()

# Create a new collection
    collection_name = dbName["MongoProjectMaster"]
    item_details = collection_name.find({"ProjectId": 1}, {"ProjectName": 1})
    data = []
    for item in item_details:
        # print(item)
        data.append(item)
    return data


def insertProject(document):
    dbName = get_database()
    
    collection = dbName["YorientTable"]
    doc = collection.insert_one(document=document)
    return doc

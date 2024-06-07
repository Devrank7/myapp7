from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://mongo:mgdb7@cluster0.d700lsf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


def get_nosql_database():
    client = MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client.Boobna
    except Exception as e:
        print("Does not OK")
        print(e)

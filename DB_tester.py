from pymongo import MongoClient
import os
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

load_dotenv()

mongo_uri= os.getenv("mongoDB_uri")

if not mongo_uri:
    raise ValueError("Environment variable 'MongoDB_uri' is not set ")

try:
    client = MongoClient(mongo_uri)
    client.admin.command('ping')
    print("Connection successful")

    db = client["test_atlas"]

    collections = db.list_collection_names()

    if collections:
        print("Collections found", collections)

    else:
        print("No collections found")


except ConnectionFailure as e:
    print("connection failed", e)

except Exception as ex:
    print("an error occured", ex)



# client = MongoClient(uri, server_api=ServerApi('1'))
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
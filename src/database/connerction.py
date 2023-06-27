from dotenv import find_dotenv, load_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

PASSWORD = os.environ.get("MONGODB_PWD") 
USERNAME = os.environ.get("MONGODB_USER")

connection_string = f"mongodb://{USERNAME}:{PASSWORD}@localhost:27017/"

client = MongoClient(connection_string)
my_app_db = client["my-app"]
collection = my_app_db["user"]

if __name__ == "__main__":
    dbs = client.list_database_names()
    my_app_db = client["my-app"]
    collections = my_app_db.list_collection_names()
    print(dbs)
    print(collections)
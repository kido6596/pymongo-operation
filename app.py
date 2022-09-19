import pymongo
from pymongo import MongoClient
cluster = pymongo.MongoClient("mongodb+srv://kidosol6596:297de1297de1@cluster0.rif4pqu.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

post = {"_id": 0, "name": "sarah", "score": 5}

collection.insert_one(post)
import pymongo
from pymongo import MongoClient

def database():
    client = MongoClient(host="mongodb")
    db = client.registre
    return db
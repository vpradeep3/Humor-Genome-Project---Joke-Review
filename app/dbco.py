from pymongo import MongoClient

DBNAME = 'scribe'

client = MongoClient('mongodb://localhost:27017/')

db = client[DBNAME]

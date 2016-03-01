from pymongo import MongoClient
from flask import Flask

DBNAME = 'scribe'

client = MongoClient()

db = client.joke_review

joke_coll = db.jokes

joke_1 = {"Joke": "Why did the chicken cross the road? Because he is stupid."}

joke_json = Flask.jsonify(**joke_1)

result = joke_coll.insert_one(joke_json)




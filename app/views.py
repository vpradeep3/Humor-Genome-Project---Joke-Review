from app import app
from flask import render_template
import jokes
from pymongo import MongoClient
import pymongo
from flask import Flask
import flask


@app.route('/')
@app.route('/index')
def index():

    print("hello")
    client = MongoClient('mongodb://localhost:27017/')

    db = client.joke_review

    joke_coll = db.jokes


    result_1 = joke_coll.insert_one({
        "joke" : "Just changed my Facebook name to \'No one\' so when I see stupid posts I can click like and it will say \'No one\' likes this'."
    })

    result_2 = joke_coll.insert_one({
        "joke" : "What's the difference between snowmen and snowladies? Snowballs"
    })

    result_3 = joke_coll.insert_one({
        "joke" : "How do you make holy water? You boil the hell out of it"
    })

    cursor = db.jokes.find().sort([
        ("joke", pymongo.ASCENDING),
    ])
    jokesList = []
    i = 0
    for joke in cursor:
        print(joke)
        joke_string = joke["joke"]
        joke_id = joke["_id"]
        new_joke = jokes.Joke(joke_string, joke_id)
        jokesList.append(new_joke)

    return render_template('index.html',title ='Joke Review', jokes = jokesList)

from app import app
from flask import render_template
import jokes

@app.route('/')
@app.route('/index')
def index():
    jokesList = [jokes.Joke("Just changed my Facebook name to \'No one\' so when I see stupid posts "
                        "I can click like and it will say \'No one\' likes this'.", 1),
             jokes.Joke("What's the difference between snowmen and snowladies? Snowballs",2),
             jokes.Joke("How do you make holy water? You boil the hell out of it",3)]
    return render_template('index.html',title ='Joke Review', jokes = jokesList)

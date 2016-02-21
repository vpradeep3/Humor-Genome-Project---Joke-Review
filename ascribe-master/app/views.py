from app import app
from flask import render_template
import notes

@app.route('/')
@app.route('/index')
def index():
    jokes = [notes.Note("Just changed my Facebook name to \'No one\' so when I see stupid posts "
                        "I can click like and it will say \'No one\' likes this'.", 1),
             notes.Note("What's the difference between snowmen and snowladies? Snowballs",2),
             notes.Note("How do you make holy water? You boil the hell out of it",3)]
    return render_template('index.html',title ='Joke Review', jokes = jokes)

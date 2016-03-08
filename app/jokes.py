import random

field_content = 'content'
field_jokeId = 'jokeId'
field_title = 'title'


class Joke(object):

    def __init__(self, content, title, jokeId=None):

        self.content = str(content)

        if jokeId is None:
            jokeId = random.randint(54321, 16171617)

        self.jokeId = jokeId
        
        self.title = title;


    def to_json(self):
        myjoke = dict()

        myjoke[field_content] = self.content
        myjoke[field_jokeId] = self.jokeId
        myjoke[field_title] = self.title
        
        return myjoke

    @classmethod
    def from_json(constructor, joke):

        self.content = joke[field_content]
        self.jokeId = joke[field_jokeId]
        self.title = joke[field_title]
        

        return constructor(content, jokeId)

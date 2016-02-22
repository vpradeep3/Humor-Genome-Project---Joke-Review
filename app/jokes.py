import random

field_content = 'content'
field_jokeId = 'jokeId'


class Joke(object):

    def __init__(self, content, jokeId=None):

        self.content = str(content)

        if jokeId is None:
            jokeId = random.randint(54321, 16171617)

        self.jokeId = jokeId


    def to_json(self):
        myjoke = dict()

        myjoke[field_content] = self.content
        myjoke[field_jokeId] = self.jokeId

        return myjoke

    @classmethod
    def from_json(constructor, myuser):

        content = myuser[field_content]
        jokeId = myuser[field_jokeId]

        return constructor(content, jokeId)

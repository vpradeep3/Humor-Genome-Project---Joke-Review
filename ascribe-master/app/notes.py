import random

field_content = 'content'
field_noteId = 'noteId'

class Note(object):

    def __init__(self, content, noteId=None):

        self.content = str(content)

        if noteId is None:
            noteId = random.randint(54321, 16171617)

        self.noteId = noteId


    def to_json(self):
        mynote = dict()

        mynote[field_content] = self.content
        mynote[field_noteId] = self.noteId

        return mynote

    @classmethod
    def from_json(constructor, myuser):

        content = myuser[field_content]
        noteId = myuser[field_noteId]

        return constructor(content, noteId)

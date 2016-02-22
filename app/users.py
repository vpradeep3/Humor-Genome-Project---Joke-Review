import random

field_fname = 'fname'
field_lname = 'lname'
field_email = 'email'
field_password = 'password'
field_userId = 'userId'

class User(object):

    def __init__(self, fname, lname, email, password, userId=None):
        if not all([fname, lname, email, password]):
                raise ValueError

        self.fname = str(fname)
        self.lname = str(lname)
        self.email = str(email)
        self.password = str(password)

        if userId is None:
            userId = random.randint(12345, 998765)

        self.userId = userId


    def to_json(self):
        myuser = dict()

        myuser[field_fname] = self.fname
        myuser[field_lname] = self.lname
        myuser[field_email] = self.email
        myuser[field_password] = self.password
        myuser[field_userId] = self.userId

        return myuser

    @classmethod
    def from_json(constructor, myuser):
        fname = myuser[field_fname]
        lname = myuser[field_lname]
        email = myuser[field_email]
        password = myuser[field_password]
        userId = myuser.get(field_userId)

        return constructor(fname, lname, email, password, userId)

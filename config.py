import os

class Config(object):
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'you_will_never_guess'

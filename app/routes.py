from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Hari'}
    posts = [
        {
            'author': 'Sneha',
            'body': 'Python is cool!',
        },
        {
            'author': 'Sundar',
            'body': 'js is cooler',
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

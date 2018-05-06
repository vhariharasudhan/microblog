from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
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
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Incorrect username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next = request.args.get('next')
        if not next or url_parse(next).netloc != '':
            return redirect(url_for('index'))
        return redirect(next)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        u = User(username=form.username.data, email=form.email.data)
        u.set_password(form.password1.data)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

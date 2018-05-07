from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, FileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User
from app import app

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('ConfirmPassword', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please choose a different username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please choose a different email')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    profile_pic = FileField('Profile photo', validators=[FileAllowed(set(app.config['ALLOWED_EXTENSIONS']))])
    submit = SubmitField('Submit')

class FileUploadForm(FlaskForm):
    csv_file = FileField('Upload a CSV File', validators=[FileAllowed(['csv'], 'Only csv files are supported'), FileRequired()])
    submit = SubmitField('Analyze')

class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')

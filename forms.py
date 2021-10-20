from wtforms import Form,StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length
from flask_wtf import FlaskForm
from flask import *


class LoginForm(Form):
    username = StringField('Username',validators=[DataRequired(message='Not empty!')])
    password = PasswordField('Password',validators=[DataRequired(),Length(8,128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


form = LoginForm()

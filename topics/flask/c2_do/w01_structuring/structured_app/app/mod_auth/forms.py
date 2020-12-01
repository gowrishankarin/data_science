# Import Form and RecatchaField 
from flask_wtf import FlaskForm, RecaptchaField

from wtforms import TextField, PasswordField

# Import form elements such as TextField and BooleanField 
from wtforms.validators import Required, Email, EqualTo

# Define the login form (WTForms)

class LoginForm(FlaskForm):
    email    = TextField('Email Address', [Email(),
                Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
                Required(message='Must provide a password. ;-)')]) 
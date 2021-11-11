from flask_wtf import FlaskForm
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required,Email,EqualTo
from ..models import Pitch, User
from wtforms import ValidationError
from wtforms import StringField,PasswordField,BooleanField,SubmitField

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    category=StringField('Pitch Category', validators=[Required()])
    Pitch = TextAreaField('New Pitch', validators=[Required()])
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
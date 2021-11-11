from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required,Email,EqualTo
from ..models import Pitch, User


class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    category=StringField('Pitch Category', validators=[Required()])
    Pitch = TextAreaField('New Pitch', validators=[Required()])
    submit = SubmitField('Submit')
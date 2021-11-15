
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email





class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    category=StringField('Pitch Category', validators=[Required()])
    Pitch = TextAreaField('New Pitch', validators=[Required()])
    submit = SubmitField('Submit')
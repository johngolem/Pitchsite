
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required,Email





class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    category = SelectField('Category', choices=[('pickup-lines','pickup'),('interview','interview'),('product','product'),('promotion','promotion')],validators=[Required()])
    post = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Submit')
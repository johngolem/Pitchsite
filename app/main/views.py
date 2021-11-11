from . import main
from flask import render_template
from flask_login import login_required
from ..models import Pitch
from ..auth import PitchForm


# Pitch = pitch.Pitch

@main.route('/')
def index ():
    return render_template("index.html")

@main.route('/pitch//new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    form = PitchForm()
#     pitch = get_pitch(id)

    if form.validate_on_submit():
        title = form.title.data
        category = form.pitch.data
     #    new_pitch = Pitch(movie.id,title,movie.poster,review)
        new_pitch.save_pitch()
     #    return redirect(url_for('movie',id = movie.id ))

#     title = f'{movie.title} review'
#     return render_template('new_pitch.html',title = title, pitch_form=form, pitch=pitch)
    



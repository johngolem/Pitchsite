from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from ..models import Pitch,User
from .forms import  PitchForm,UpdateProfile
from .. import db
from .forms import UpdateProfile,PitchForm



# Pitch = pitch.Pitch

@main.route('/')
def index ():
    p="Hello World"
    pitches = Pitch.query.all()
    pickuplines = Pitch.query.filter_by(category = 'pickuplines').all() 
    # business = Pitch.query.filter_by(category = 'Business').all()
    interview = Pitch.query.filter_by(category = 'interview').all()
    product = Pitch.query.filter_by(category = 'product').all()
    promotion = Pitch.query.filter_by(category = 'promotion').all()
    # social = Pitch.query.filter_by(category = 'Social').all()
    return render_template('index.html', pitches = pitches, pickuplines = pickuplines ,interview = interview, product = product, promotion= promotion,)

# @main.route('/pitch//new/<int:id>', methods = ['GET','POST'])
@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch(id):
    form = PitchForm()

    if form.validate_on_submit():
        title = form.title.data
        category = form.pitch.data
     #    new_pitch = Pitch(movie.id,title,movie.poster,review)
        new_pitch.save_pitch()
     #    return redirect(url_for('movie',id = movie.id ))

#     title = f'{movie.title} review'
#     return render_template('new_pitch.html',title = title, pitch_form=form, pitch=pitch)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
    
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)




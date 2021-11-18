from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from ..models import Pitch,User
from .forms import  PitchForm,UpdateProfile
from .. import db
from .forms import UpdateProfile,PitchForm



# Pitch = pitch.Pitch

@main.route('/')
def index ():
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
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('new_pitch.html', form = form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
    
@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)



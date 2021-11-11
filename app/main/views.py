from . import main
from flask import render_template
from flask_login import login_required


@main.route('/')
def index ():
     '''
    View root page function that returns the index page and its data
    '''

@main.route('/pitch//new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):

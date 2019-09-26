from flask import render_template, url_for,request,redirect, abort
from flask_login import login_required,current_user, login_user, logout_user
from . import main
from .. import db
from app.models import *
import requests

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/projects', methods=['GET','POST'])
def projects():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        progress = form.get('progress')
        period = form.get('period')
        image = form .get('image')
        description = form.get('description')
        if name==None or progress==None or period==None or image==None or description==None:
            error = "Kindly fill all fields to continue"
            return render_template('projects.html', error=error)
        project = Projects(name=name,progress=progress,period=period,image=image,description=description, user_id=current_user.id)
        project.save()
        return redirect(url_for('main.index'))
    return render_template('projects.html')


@main.route('/profile', methods=['POST','GET'])
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    projects = Project.query.filter_by(user_id = current_user.id).first()
    return render_template('projects.html', user=user, projects = projects)

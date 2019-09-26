from flask import render_template, url_for,request,redirect, abort
from flask_login import login_required,current_user, login_user, logout_user
from . import main
from .. import db
from ..models import User,Project,Comment
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
        projectTimeline = form.get('projectTimeline')
        project_photo = form .get('project_photo')
        description = form.get('description')
        if name==None or progress==None or projectTimeline==None or project_photo==None or description==None:
            error = "Kindly fill all fields to continue"
            return render_template('projects.html', error=error)
        projects = Project(name=name, progress=progress, projectTimeline=projectTimeline, project_photo=project_photo, description=description, miradi=current_user)
        projects.save()
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

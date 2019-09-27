from flask import render_template, url_for,request,redirect, abort
from flask_login import login_required,current_user, login_user, logout_user
from . import main
from .. import db,photos
from app.models import *
import requests

@main.route('/home')
@login_required
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@main.route("/")
def landing():
    return render_template("home.html")


@main.route('/projoprofile')
@login_required
def projoprofile():
    projects = Project.query.all()
    return render_template('projoprofile.html', projects=projects)



@main.route('/projects', methods=['GET','POST'])
def projects():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        progress = form.get('progress')
        projectTimeline = form.get('projecttimeline')
        project_photo = form .get('project_photo')
        description = form.get('description')
        if name==None or progress==None or projectTimeline==None or project_photo==None or description==None:
            error = "Kindly fill all fields to continue"
            return render_template('projects.html', error=error)
        project = Project(name=name,progress=progress,projectTimeline=projectTimeline,project_photo=project_photo,description=description, user_id=current_user.id)
        project.save()
        return redirect(url_for('main.index'))
    return render_template('projects.html')

@main.route('/project/<pname>/update/pic',methods= ['POST'])
@login_required
def update_pic(pname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/photo')
@login_required
def photo():
    project = Project.query.filter_by(name=name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'images/{filename}'
        project.project_photo = path
        db.session.commit()
        return redirect('main.projoprofile')


@main.route('/profile', methods=['POST','GET'])
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    projects = Project.query.filter_by(user_id = current_user.id).first()
    return render_template('projects.html', user=user, projects = projects)

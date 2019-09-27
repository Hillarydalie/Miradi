from flask import render_template, url_for,request,redirect, abort
from flask_login import login_required,current_user, login_user, logout_user
from . import main
from .. import db, photos
from app.models import *
import requests

@main.route('/home')
@login_required
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects,)

@main.route("/")
def landing():
    return render_template("home.html")


@main.route('/projoprofile')
@login_required
def projoprofile():
    projects = Project.query.all()
    comments = Comment.query.all()
    return render_template('projoprofile.html', projects=projects, comments=comments)



@main.route('/projects', methods=['GET','POST'])
def projects():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        progress = form.get('progress')
        projectTimeline = form.get('projecttimeline')
        project_photo = form .get('project_photo')
        description = form.get('description')
        if name==None or progress==None or projectTimeline==None or description==None:
            error = "Kindly fill all fields to continue"
            return render_template('projects.html', error=error)
        project = Project(name=name,progress=progress,projectTimeline=projectTimeline,project_photo=project_photo,description=description, user_id=current_user.id)
        project.save()
        return redirect(url_for('main.index'))
    return render_template('projects.html')



@main.route('/photo/<uname>', methods=['POST','GET'])
@login_required
def photo(uname):
    project = Project.query.filter_by(name=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'images/{filename}'
        project.project_photo = path
        db.session.commit()
    return redirect(url_for('main.projoprofile', uname=uname))


@main.route('/profile', methods=['POST','GET'])
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    projects = Project.query.filter_by(user_id = current_user.id).first()
    return render_template('projects.html', user=user, projects = projects)




@main.route('/comment/<int:project_id>', methods=['GET','POST'])
def comment(project_id):
    if request.method == 'POST':
        report = request.form.get('report')
        user_id = current_user.id
        project = Project.query.filter_by(id=project_id).first()
        comment = Comment(report=report,project_id=project.id,user_id=user_id)
        comment.save()
        return redirect(url_for('main.comment',project_id=project_id))
    return render_template('projoprofile.html')

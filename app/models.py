from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique = True)
    password = db.Column(db.String(255), nullable=False)
    image =db.Column(db.Photo)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    projects = db.relatiships('Project', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'

class Project(db.Model):
    __tablename__="projects"
    id = db.Column(db.Integer, primary_key = False)
    name = db.Column(db.String(255), unique = False)
    projectTimeline = db.Column(db.String(255), nullable=False)
    image = db.Column(db.Photo)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    comments = db.relationship('Comment', backref='project', lazy='dynamic')
    

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, default=datetime.time)
    report = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    project_id = db.Colum(db.Integer, db.ForeignKey('projects.id'), nullable = False)
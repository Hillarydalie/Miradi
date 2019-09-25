from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True)
    password = db.Column(db.String(255))
    image =db.Column(db.Photo)

    def __repr__(self):
        return f'User {self.username}'

class Project(db.Model):
    __tablename__="projects"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique = True)
    projectTimeline = db.Column(db.String(255))
    image = db.Column(db.Photo)
    description = db.Column(db.TextField)
    

class Comment(db.Model):
    __tablename__ = "comments"
from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary)

class Project(db.Model):
    __tablename__="projects"

class Comment(db.Model):
    __tablename__ = "comments"
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
    user_image = db.Column(db.String(255))
    comments = db.relationship('Comment', backref='miradi', lazy='dynamic')
    projects = db.relationship('Project', backref='miradi', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self, password):
        password_hash = generate_password_hash(password)
        self.password = password_hash

    def check_password(self,password):
        return check_password_hash (self.password, password)

    def __repr__(self):
        return f'User {self.username}'

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class Project(db.Model):
    __tablename__="projects"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique = False)
    progress = db.Column(db.Text)
    projectTimeline = db.Column(db.String(255), nullable=False)
    project_photo = db.Column(db.String(255))
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    comments = db.relationship('Comment', backref='usercomment', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Project {self.name}'

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    report = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable = False)


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comment {self.date}'

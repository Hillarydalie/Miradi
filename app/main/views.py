from flask import render_template, url_for,request,redirect
from flask_login import login_required,current_user
from . import main
from .. import db

@main.route('/')
def home():
    return render_template('index.html')

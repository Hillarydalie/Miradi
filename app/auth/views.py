from flask import render_template,request,redirect,url_for
from flask_login import login_user,logout_user
from . import auth
from app.models import User

@auth.route('/authentication/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')

        user = User.query.filter_by(username=username).first()

        if user==None:
            error = "user with that username or password does not exist"
            return render_template('login.html',error=error)
        is_correct_password == user.check_password(password)
        if is_correct_password == False:
            error = "Wrong password"
            return render_template('login.html',error=error)
        
        login_user(user)
        return redirect(url_for('main.index'))
    return render_template('login.html')

@auth.route('/authentication/sign-up',methods=['GET','POST'])
def signup():





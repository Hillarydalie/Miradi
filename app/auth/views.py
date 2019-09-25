from flask import render_template,request,redirect,url_for
from flask_login import login_user,logout_user
from . import auth
from app.models import User

@auth.route('/login',methods=['GET','POST'])
def login():
    















# from flask import render_template, request,redirect,url_for
# from . import auth
# from app.models import User
# from flask_login import login_user,logout_user

# @auth.route('/login',methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         form = request.form
#         username= form.get('username')
#         password = form.get('password')

#         user = User.query.filter_by(username=username).first()

#         if user == None:
#             error = "user with that username or password does not exist"
#             return render_template('login.html',error = error)
#         is_correct_password = user.check_password(password)
#         if is_correct_password == False:
#             error="user with that username or password does not exist"
#             return render_template('login.html',error = error)

#         login_user(user)
#         return redirect(url_for('main.index'))
#     return render_template("login.html")

# @auth.route('/sign-up',methods=['GET','POST'])
# def signup():

#     if request.method == 'POST':
#         form = request.form
#         username = form.get("username")
#         email = form.get("email")
#         password = form.get("password")
#         confirm_password = form.get("confirm_password")

#         if username==None or password==None or email==None or confirm_password==None:
#             error="Fill in the fields"
#             return render_template("signup.html",error=error)

#         if " " in username:
#             error = "username can not be empty"
#             return render_template("signup.html",error=error)

#         if password != confirm_password:
#             error = "Passwords do not match"
#             return render_template("signup.html",error=error)
#         else:
#             user = User.query.filter_by(username=username).first()
#             if user != None:
#                 error = "user with that username already exist"
#                 return render_template("signup.html",error=error)

#             user = User.query.filter_by(email=email).first()
#             if user != None:
#                 error = "user with that email already exist"
#                 return render_template("signup.html",error=error)

#             user = User(username=username,email=email)
#             user.set_password(password)
#             user.save()
#             return redirect(url_for("auth.login"))

#         print(username)
        
#     return render_template("signup.html")

# @auth.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('auth.login'))
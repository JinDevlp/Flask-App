from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user


auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    # request.form will have all of the data that was sent 
    if request.method == 'POST':
        username = request.form.get('user_name')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        # user_projects = user.current_projects
        # for project in user_projects:
        #     project.id
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully!', category ='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again!', category ='error')
        else:
            flash('Username does not exist', category='error')
            
    return render_template('login.html',user = current_user)
    # you can access variable text from login.html


@auth.route('/logout')
@login_required
def logout(): 
    logout_user()
    return redirect(url_for('auth.login'))



@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        username = request.form.get('user_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # user = User.query.filter_by(username=username).first()
        # if user:
        #     flash('User already exists.', category='error')      
        if len(email) < 4:
            flash('email must be longer than 4 characters',category='error')
        elif len(first_name) < 2:
            flash('first name need to be longer 2 characters', category='error')
        elif password1 != password2:
            flash('passwords don\'t match',category='error')
        elif len(password1) < 7:
            flash('password must be longer than 7 characters',category='error')
        elif db.session.query(User).filter_by(username=username).count() < 1:
            user = User(email=email,first_name=first_name,username=username, password = generate_password_hash(password1, method='sha256'))
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('User already exists.', category='error')
            
            
    return render_template('sign_up.html',user=current_user)


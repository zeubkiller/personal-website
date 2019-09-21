from flask import render_template, flash, redirect, url_for

from flask_login import current_user, login_user

from app import serverApp
from app.forms import LoginForm

@serverApp.route("/")
@serverApp.route("/index")
def hello():
    user = {"username" : "George"}
    return render_template('index.html', title="Home", user=user)

@serverApp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for("index"))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.username.data).first
        if user is None or not user.is_authenticated(form.data.password)
            flash("Invalid username or password")
            return redirect(url_for("login"))
        
        login_user(user, remember=form.remember_me.data)
        redirect(url_for("index"))
    return render_template('login.html', title='Sign In', form=form)
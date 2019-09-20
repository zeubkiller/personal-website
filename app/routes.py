from flask import render_template, flash, redirect

from app import serverApp
from app.forms import LoginForm

@serverApp.route("/")
@serverApp.route("/index")
def hello():
    user = {"username" : "George"}
    return render_template('index.html', title="Home", user=user)

@serverApp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me {}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
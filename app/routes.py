from flask import render_template

from app import serverApp
from app.forms import LoginForm

@serverApp.route("/")
@serverApp.route("/index")
def hello():
    user = {"username" : "George"}
    return render_template('index.html', title="Home", user=user)

@serverApp.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
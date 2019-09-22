from flask import render_template

from flask_login import login_required

from app import serverApp

@serverApp.route("/")
@serverApp.route("/index")
@login_required
def index():
    posts = []
    return render_template('index.html', title="Home", posts=posts)


from app import serverApp
from flask import render_template

@serverApp.route("/")
@serverApp.route("/index")
def hello():
    user = {"username" : "George"}
    return render_template('index.html', title="Home", user=user)
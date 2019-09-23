from flask import render_template

from flask_login import login_required

from app.main import main_bp

@main_bp.route("/")
@main_bp.route("/index")
@login_required
def index():
    posts = []
    return render_template('index.html', title="Home", posts=posts)


from flask import render_template, flash, redirect, url_for, request

from werkzeug.urls import url_parse

from flask_login import current_user, login_user, logout_user, login_required

from app.application import database_instance
from app.authentification import auth_bp
from app.authentification.forms import LoginForm, RegistrationForm
from app.database.user_model import User

@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.is_password_ok(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("authentification.login"))
        
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != '': #Will check if the next argument is empty or if the next argument redirect to an external webpage
            next_page = url_for("main.index")

        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth_bp.route("/register",  methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    
    register_form = RegistrationForm()

    if register_form.validate_on_submit():
        new_user = User(username=register_form.username.data, email=register_form.email.data)
        new_user.set_password_hash(register_form.password.data)
        database_instance.session.add(new_user)
        database_instance.session.commit()

        flash("Congratulation you are a new user")
        return redirect(url_for("authentification.login"))

    return render_template('register.html', title="Register", form=register_form)
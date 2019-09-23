from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from app.application import database_instance, login

class User(UserMixin, database_instance.Model):
    id = database_instance.Column(database_instance.Integer, primary_key=True)
    username = database_instance.Column(database_instance.String(64), index=True, unique=True)
    email = database_instance.Column(database_instance.String(120), index=True, unique=True)
    password_hash = database_instance.Column(database_instance.String(128), index=True, unique=True)
    posts = database_instance.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<user>{}'.format(self.username)

    def set_password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def is_password_ok(self, current_password):
        return check_password_hash(self.password_hash, current_password)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Post(database_instance.Model):
    id = database_instance.Column(database_instance.Integer, primary_key=True)
    body = database_instance.Column(database_instance.String(140), index=True)
    timestamp = database_instance.Column(database_instance.DateTime, index=True, default=datetime.utcnow)
    user_id = database_instance.Column(database_instance.Integer, database_instance.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
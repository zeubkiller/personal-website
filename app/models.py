from datetime import datetime

from app import database_instance

class User(database_instance.Model):
    id = database_instance.Column(database_instance.Integer, primary_key=True)
    username = database_instance.Column(database_instance.String(64), index=True, unique=True)
    email = database_instance.Column(database_instance.String(120), index=True, unique=True)
    password_hash = database_instance.Column(database_instance.String(128), index=True, unique=True)
    posts = database_instance.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<user>{}'.format(self.username)

class Post(database_instance.Model):
    id = database_instance.Column(database_instance.Integer, primary_key=True)
    body = database_instance.Column(database_instance.String(140), index=True)
    timestamp = database_instance.Column(database_instance.DateTime, index=True, default=datetime.utcnow)
    user_id = database_instance.Column(database_instance.Integer, database_instance.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
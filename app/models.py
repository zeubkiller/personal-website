from app import database_instance

class User(database_instance.Model):
    id = database_instance.Column(database_instance.Integer, primary_key=True)
    username = database_instance.Column(database_instance.String(64), index=True, unique=True)
    email = database_instance.Column(database_instance.String(120), index=True, unique=True)
    password_hash = database_instance.Column(database_instance.String(128), index=True, unique=True)

    def __repr__(self):
        return '<user>{}'.format(self.username)
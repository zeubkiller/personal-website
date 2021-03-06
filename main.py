
from app import serverApp
from app.application import database_instance
from app.database.user_model import User, Post

@serverApp.shell_context_processor
def make_shell_context():
    return {'db' : database_instance, 'User': User, 'Post': Post}
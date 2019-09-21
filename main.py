
from app import serverApp, database_instance
from app.models import User, Post

@serverApp.shell_context_processor
def make_shell_context():
    return {'db' : database_instance, 'User': User, 'Post': Post}
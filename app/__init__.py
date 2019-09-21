from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

from app.configurations import ServerConfiguration

serverApp = Flask(__name__)
serverApp.config.from_object(ServerConfiguration)
serverApp.debug = True


database_instance = SQLAlchemy(serverApp)
migrate_instance = Migrate(serverApp, database_instance)

login = LoginManager(serverApp)
login.login_view = "login"

from app import routes, models
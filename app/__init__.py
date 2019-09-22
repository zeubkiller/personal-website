import os
import logging
from flask import Flask

from logging.handlers import RotatingFileHandler

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from app.configurations import ServerConfiguration

serverApp = Flask(__name__)
serverApp.config.from_object(ServerConfiguration)

database_instance = SQLAlchemy(serverApp)
migrate_instance = Migrate(serverApp, database_instance)

login = LoginManager(serverApp)
login.login_view = "authentification.login"

bootstrap = Bootstrap(serverApp)

from app.authentification import auth_bp
serverApp.register_blueprint(auth_bp)

from app import routes, models, errors
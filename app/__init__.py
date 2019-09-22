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

if not serverApp.debug:
    if not os.path.exists("logs"):
        os.mkdir("logs")
    file_handler = RotatingFileHandler("logs/app.log", maxBytes=10240, backupCount=10)

    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)

    serverApp.logger.addHandler(file_handler)

    serverApp.logger.setLevel(logging.INFO)
    serverApp.logger.info("App startup")

database_instance = SQLAlchemy(serverApp)
migrate_instance = Migrate(serverApp, database_instance)

login = LoginManager(serverApp)
login.login_view = "login"

bootstrap = Bootstrap(serverApp)

from app import routes, models, errors
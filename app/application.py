import os
import logging

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from logging.handlers import RotatingFileHandler

from app.configurations import ServerConfiguration

database_instance = SQLAlchemy()
migrate_instance = Migrate()
login = LoginManager()
bootstrap = Bootstrap()


class ServerApplication(object):

    @staticmethod
    def initialize_server():
        serverApp = Flask(__name__)

        serverApp.config.from_object(ServerConfiguration)

        if not serverApp.debug:
            ServerApplication.configure_log_to_file(serverApp)

        return serverApp

    @staticmethod
    def initialize_dependencies(serverApp):
        #Dependency creation
        database_instance.init_app(serverApp)
        migrate_instance.init_app(serverApp, database_instance)

        login.init_app(serverApp)
        login.login_view = "authentification.login"

        bootstrap.init_app(serverApp)

    @staticmethod
    def configure_log_to_file(serverApp):
            if not os.path.exists("logs"):
                os.mkdir("logs")
            file_handler = RotatingFileHandler("logs/app.log", maxBytes=10240, backupCount=10)

            file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)

            serverApp.logger.addHandler(file_handler)

            serverApp.logger.setLevel(logging.INFO)
            serverApp.logger.info("App startup")

    @staticmethod
    def blueprint_registration(serverApp):
        from app.main import main_bp
        serverApp.register_blueprint(main_bp)

        from app.authentification import auth_bp
        serverApp.register_blueprint(auth_bp)

        from app.error import error_bp
        serverApp.register_blueprint(error_bp)


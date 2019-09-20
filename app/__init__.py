from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.configurations import ServerConfiguration

serverApp = Flask(__name__)
serverApp.config.from_object(ServerConfiguration)

database_instance = SQLAlchemy(serverApp)
migrate = Migrate(serverApp, database_instance)

from app import routes, models
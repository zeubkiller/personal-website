from flask import Flask
from app.configurations import ServerConfiguration

serverApp = Flask(__name__)
serverApp.config.from_object(ServerConfiguration)


from app import routes
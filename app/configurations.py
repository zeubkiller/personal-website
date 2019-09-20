import os

class ServerConfiguration(object):
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'gaston-bore-est-mon-pere'
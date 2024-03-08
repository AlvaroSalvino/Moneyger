import os


class Config():
    CSRF_ENABLE = True
    SECRET = 'TI-MALTA'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None


class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%$/%$' % (IP_HOST, PORT_HOST)  # http://localhost:8000
    SQLALCHEMY_DATABASE_URI = ''


app_config = {
    'development': DevelopmentConfig(),
    'testing': None
}

app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'development'

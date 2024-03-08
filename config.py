import os


class Config():
    CSRF_ENABLE = True
    SECRET = 'T159I159M159A159L159T159A159'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None


class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)  # http://localhost:8000
    SQLALCHEMY_DATABASE_URI = ''


class TestingConfig(Config):
    pass


app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig()
}

app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'development'

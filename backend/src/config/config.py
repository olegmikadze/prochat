import os

basedir = os.path.abspath(os.path.dirname('../'))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgres://oleg:1@localhost:5432/prochat_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class TestingConfig(Config):
    TESTING = True

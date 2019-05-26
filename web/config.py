# @see http://flask.pocoo.org/docs/0.12/api/

import os
import logging

_basedir = os.path.abspath(os.path.dirname(__file__))

class AppConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gee3Woh3iew2oj8ueZieCheebieTiw5g'
    LOG_FILE = _basedir+'/logs/flaskapp.log'
    LOG_LEVEL = logging.ERROR  # CRITICAL,ERROR,WARNING,INFO,DEBUG,NOTSET
    BOOTSTRAP_USE_MINIFIED = True
    BOOTSTRAP_SERVE_LOCAL = True
    MYSQL_USER = os.environ.get('DB_USER') or 'root'
    MYSQL_PASSWORD = os.environ.get('DB_PASSWORD') or ''
    MYSQL_DB = os.environ.get('DB_NAME') or 'testing'
    MYSQL_HOST = os.environ.get('DB_HOST') or '127.0.0.1'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://'+MYSQL_USER+':'+MYSQL_PASSWORD+'@'+MYSQL_HOST+'/'+MYSQL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = 30
    SQLALCHEMY_MAX_OVERFLOW = 2

    # user.user_role
    USER_ROLE_NONE = 0
    USER_ROLE_VIEW = 1
    USER_ROLE_EDIT = 2
    USER_ROLE_ADMIN = 3
    USER_ROLE = {
        USER_ROLE_NONE: 'Inactive',
        USER_ROLE_VIEW: 'User',
        USER_ROLE_EDIT: 'Editor',
        USER_ROLE_ADMIN: 'Administrator',
    }
    # item.item_status
    ITEM_STATUS_HIDDEN = 0
    ITEM_STATUS_DRAFT = 1
    ITEM_STATUS_COMPLETED = 2
    ITEM_STATUS_APPROVED = 3
    ITEM_STATUS = {
        ITEM_STATUS_HIDDEN: 'Hidden',
        ITEM_STATUS_DRAFT: 'Draft',
        ITEM_STATUS_COMPLETED: 'Completed',
        ITEM_STATUS_APPROVED: 'Approved',
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(AppConfig):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_RECORD_QUERIES = True


class TestingConfig(AppConfig):
    TESTING = True
    LOG_LEVEL = logging.INFO
    #SQLALCHEMY_ECHO = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(AppConfig):
    DEBUG = False
    TESTING = False
    LOG_LEVEL = logging.WARNING

    @classmethod
    def init_app(cls, app):
        # multi-step setups could go here
        AppConfig.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing':     TestingConfig,
    'production':  ProductionConfig,
    'default':     DevelopmentConfig
}

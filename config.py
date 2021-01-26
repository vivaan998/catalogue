import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    MYSQL_DATABASE_USER = 'webserver'
    MYSQL_DATABASE_PASSWORD = 'webserver'
    MYSQL_DATABASE_DB = 'db'
    MYSQL_DATABASE_HOST = "mysql"


class DEVConfig(object):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = False
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'password'
    MYSQL_DATABASE_DB = 'db'
    MYSQL_DATABASE_HOST = "localhost"

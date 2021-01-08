from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine

from . import model

import threading

lock = threading.Lock()


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Db(metaclass=Singleton):
    def __init__(self, app):
        connection_str = 'mysql+pymysql://{0}:{1}@{2}:3306/{3}'.format(
            app.config['MYSQL_DATABASE_USER'],
            app.config['MYSQL_DATABASE_PASSWORD'],
            app.config['MYSQL_DATABASE_HOST'],
            app.config['MYSQL_DATABASE_DB'])
        self.engine = create_engine(connection_str, echo=app.config['DEBUG'], pool_size=100, pool_recycle=3600)
        self.session_factory = sessionmaker(bind=self.engine)
        self.session = scoped_session(self.session_factory)
        self.model = model

from flask import Flask
from src.dal.db import Db
from src.catalogue.session.api import bp_session
from src.catalogue.categories.api import bp_categories
import config

app = Flask(__name__)
app.config.from_object(config.Config)

app.register_blueprint(bp_session, url_prefix='/api/v1/session')
app.register_blueprint(bp_categories, url_prefix='/api/v1/categories')
# TODO-2: create and register the new endpoints


@app.after_request
def after_request_func(response):
    Db().session.remove()
    return response


def init_app(flask_app):
    flask_app.config.from_object(config.DEVConfig)
    db_instance = Db(flask_app)
    print('DB Connection: ' + str(db_instance))
    print(db_instance.engine.table_names())
    print(dir(db_instance.model))


if __name__ == '__main__':
    init_app(app)
    app.run()


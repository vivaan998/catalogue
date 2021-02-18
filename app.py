import os

from flask import Flask, make_response, jsonify, request
from src.dal.db import Db
from src.catalogue.session.api import bp_session
from src.catalogue.categories.api import bp_categories
from src.catalogue.live.api import bp_live
from src.catalogue.availability.api import bp_availability
from src.catalogue.image.api import bp_image
from src.exc.app_exception import AppException, ClientException, ServerException
from flask import g
import config
# from yaml import load, Loader, dump, Dumper
# from openapi_spec_validator.schemas import read_yaml_file

# # ===== Validation 
# from openapi_core.validation.request.validators import RequestValidator
# from openapi_core.contrib.flask import FlaskOpenAPIRequest

# from openapi_core.validation.response.validators import ResponseValidator
# from openapi_core.contrib.flask import FlaskOpenAPIResponse

# from openapi_core import create_spec


# def spec_dict_from_file(spec_file):
#     directory = os.path.abspath(os.path.dirname(__file__))
#     path_full = os.path.join(directory, spec_file)
#     return read_yaml_file(path_full)


# spec_dict = spec_dict_from_file('api/api3.yaml')
# rq_validator = RequestValidator(create_spec(spec_dict))
# rs_validator = ResponseValidator(create_spec(spec_dict))

# # =====


app = Flask(__name__)
app.config.from_object(config.Config)

app.register_blueprint(bp_session, url_prefix='/api/v1/sessions')
app.register_blueprint(bp_categories, url_prefix='/api/v1/categories')
app.register_blueprint(bp_live, url_prefix='/api/v1/lives')
app.register_blueprint(bp_availability, url_prefix='/api/v1/availabilities')
app.register_blueprint(bp_image, url_prefix='/api/v1/images')


@app.errorhandler(AppException)
def app_error(err):
    app.logger.exception(err)
    return make_response(jsonify(err.error), err.http_code)


@app.errorhandler(Exception)
def handle_generic_error(err):
    app.logger.exception(err)
    return make_response(jsonify(str(err)), 500)


# @app.before_request
# def before_request_func():
#     app.logger.info("START: before_request")
#     # validate rq...

#     app.logger.info("Build FlaskOpenAPIRequest")
#     g.openapi_request = FlaskOpenAPIRequest(request)
#     app.logger.info("Validate")

#     # remove eventual trailing slash
#     fup = g.openapi_request.full_url_pattern
#     print(fup)
#     g.openapi_request.full_url_pattern = fup.rstrip('/')

#     # validate
#     result = rq_validator.validate(g.openapi_request)
#     app.logger.info("List errors")
#     app.logger.error(result.errors)
#     if len(result.errors) > 0:
#         raise ClientException("Request validation error " + str(result.errors))

#     app.logger.info("END: before_request")


# @app.after_request
# def after_request_func(response):
#     app.logger.info("START: after_request")
#     code = response.status_code
#     app.logger.info("code: {0}".format(code))

#     if code == 200 or code == 201:
#         app.logger.info("Build FlaskOpenAPIRequest")
#         openapi_response = FlaskOpenAPIResponse(response)
#         app.logger.info("Validate")
#         result = rs_validator.validate(g.openapi_request, openapi_response)
#         app.logger.info("List errors")
#         app.logger.error(result.errors)
#         if len(result.errors) > 0:
#             response = make_response(jsonify("Response validation error" + str(result.errors)), 500)

#     # Db().session.remove()
#     app.logger.info("END: after_request")
#     return response


def init_app(flask_app):
    flask_app.config.from_object(config.DEVConfig)
    db_instance = Db(flask_app)
    print('DB Connection: ' + str(db_instance))
    print(db_instance.engine.table_names())
    print(dir(db_instance.model))


if __name__ == '__main__':
    init_app(app)
    app.run(host='127.0.0.1', port='5000')

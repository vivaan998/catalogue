# Only in this file there should be reference/import to flask.
# TODO-1: Finish/correct the implementation of existing methods and add the new methods if needed
# TODO-1: Perform postman test on the methods exposed here

from flask import Blueprint, make_response
from flask import request
from flask import jsonify
from . import categories
from flask import g
from src.exc.app_exception import MissingFieldException

bp_categories = Blueprint('categories', 'categories')


@bp_categories.before_request
def before_request_func():
    # TODO-n: extract user name from the auth
    g.requestor_uuid = 1234


@bp_categories.route('/', methods=['GET'])
def get():
    if 'language' in request.args:
        languageISO = request.args.get('language')
        category = categories.get(languageISO)
        return make_response(jsonify(category), 200)
    else:
        raise MissingFieldException(' Language in the query parameter')

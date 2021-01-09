# Only in this file there should be reference/import to flask.
# TODO-1: Finish/correct the implementation of existing methods and add the new methods if needed
# TODO-1: Perform postman test on the methods exposed here

from flask import Blueprint
from flask import request
from flask import jsonify
from . import categories
from flask import g


bp_categories = Blueprint('categories', 'categories')


@bp_categories.before_request
def before_request_func():
    # TODO-n: extract user name from the auth
    g.requestor_uuid = 1243242636
    pass


@bp_categories.route('/', methods=['POST'])
def create():
    categories.create()
    return request.method+' user!'


@bp_categories.route('/', methods=['GET'])
def get():
    languageISO = request.args.get('language')
    print('>>>>> API - CATEGORIES >>> GET', languageISO)
    category = categories.get(languageISO)
    return jsonify(category)


@bp_categories.route('/<uuid>', methods=['PUT'])
def edit(uuid):
    categories.edit()
    return request.method+' user!'

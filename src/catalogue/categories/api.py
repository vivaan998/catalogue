# Only in this file there should be reference/import to flask.
# TODO-1: Finish/correct the implementation of existing methods and add the new methods if needed
# TODO-1: Perform postman test on the methods exposed here

from flask import Blueprint
from flask import request
from flask import jsonify
from . import categories
import base64
import json
from flask import g


bp_categories = Blueprint('categories', 'categories')


@bp_categories.before_request
def before_request_func():
    # TODO-n: extract user name from the auth
    # auth = request.headers['Authorization']
    # base64_bytes = auth.encode('ascii')
    # message_bytes = base64.b64decode(base64_bytes)
    # message = json.loads(message_bytes.decode('ascii'))
    # g.requestor_uuid = message['user_uuid']
    g.requestor_uuid = 1234


@bp_categories.route('/', methods=['GET'])
def get():
    if 'language' in request.args:
        languageISO = request.args.get('language')
        category = categories.get(languageISO)
        return jsonify(category)
    else:
        return jsonify({"error": True, "message": "Please select a langauge"})

# Only in this file there should be reference/import to flask.
# TODO-1: Finish/correct the implementation of existing methods and add the new methods if needed
# TODO-1: Perform postman test on the methods exposed here

from flask import Blueprint, make_response
from flask import request
from flask import jsonify
from . import session
from flask import g
from src.exc.app_exception import MissingFieldException
bp_session = Blueprint('session', 'session')


@bp_session.before_request
def before_request_func():
    # TODO-n: extract user name from the auth
    g.requestor_uuid = 1243242636
    pass


@bp_session.route('/', methods=['POST'])
def create():
    data = request.get_json()
    sessions = session.add(data)
    return make_response(jsonify(sessions), 201)


@bp_session.route('/', methods=['PUT'])
def update():
    data = request.get_json()
    sessions = session.edit(data)
    return make_response(jsonify(sessions), 202)


@bp_session.route('/', methods=['GET'])
def get():
    if 'session_uuid' in request.args:
        sessionUUID = request.args.get('session_uuid')
        sessions = session.get(sessionUUID)
        return make_response(jsonify(sessions), 200)
    else:
        raise MissingFieldException({'error': 'Session ID in the query'})


@bp_session.route('/', methods=['DELETE'])
def delete():
    if 'session_uuid' in request.args:
        sessionUUID = request.args.get('session_uuid')
        sessions = session.delete(sessionUUID)
        return make_response(jsonify(sessions), 200)
    else:
        raise MissingFieldException({'error': 'Session ID in the query'})

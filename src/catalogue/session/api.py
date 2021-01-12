# Only in this file there should be reference/import to flask.
# TODO-1: Finish/correct the implementation of existing methods and add the new methods if needed
# TODO-1: Perform postman test on the methods exposed here

from flask import Blueprint
from flask import request
from flask import jsonify
from . import session
from flask import g
import json
from ...exception.SessionException import SessionUUIDNotGiven


bp_session = Blueprint('session', 'session')


@bp_session.before_request
def before_request_func():
    # TODO-n: extract user name from the auth
    g.requestor_uuid = 1243242636
    pass


@bp_session.route('/', methods=['POST'])
def create():
    data = request.get_json()
    sessions, code = session.add(data)
    return jsonify(sessions), code

@bp_session.route('/', methods=['PUT'])
def update():
    data = request.get_json()
    sessions = session.edit(data)
    return jsonify(sessions)


@bp_session.route('/', methods=['GET'])
def get():
    if 'session_uuid' in request.args and request.args.get('session_uuid'):
        sessionUUID = request.args.get('session_uuid')
        sessions, code = session.get(sessionUUID)
        return jsonify(sessions), code
    else:
        result = SessionUUIDNotGiven()
        return result, 403


@bp_session.route('/', methods=['DELETE'])
def delete():
    if 'session_uuid' in request.args and request.args.get('session_uuid'):
        sessionUUID = request.args.get('session_uuid')
        sessions, code = session.delete(sessionUUID)
        return sessions, code
    else:
        result = SessionUUIDNotGiven()
        return result, 403
# Only in this file there should be reference/import to flask.
# TODO-1: Finish/correct the implementation of existing methods and add the new methods if needed
# TODO-1: Perform postman test on the methods exposed here

from flask import Blueprint, make_response
from flask import request
from flask import jsonify
from . import session
from flask import g
from ...dal.pagination import get_paginated_list

bp_session = Blueprint('session', 'session')


@bp_session.before_request
def before_request_func():
    # TODO-n: extract user name from the auth
    g.requestor_uuid = 1243242636


@bp_session.route('/', methods=['POST'])
def create():
    data = request.get_json()
    sessions = session.add(data)
    print(jsonify(sessions))
    return make_response(jsonify(sessions), 201)


@bp_session.route('/<session_uuid>', methods=['PUT'])
def update(session_uuid):
    data = request.get_json()
    sessions = session.edit(session_uuid, data)
    return make_response(jsonify(sessions), 202)


@bp_session.route('/<session_uuid>', methods=['GET'])
def get(session_uuid):
    sessions = session.get(session_uuid)
    return make_response(jsonify(sessions), 200)
    

@bp_session.route('/<session_uuid>/lives', methods=['GET'])
def get_lives(session_uuid):
    url = request.url
    start = request.args.get('start', 1)
    limit = request.args.get('limit', 1)
    search = request.args.get('search', None)
    lives = session.get_lives(session_uuid, search)
    return make_response(jsonify(get_paginated_list(lives, url, start, limit)), 200)


@bp_session.route('/<session_uuid>', methods=['DELETE'])
def delete(session_uuid):
    sessions = session.delete(session_uuid)
    return make_response(jsonify(sessions), 200)


@bp_session.route('/', methods=['GET'])
def get_sessions():
    url = request.url
    start = request.args.get('start', 1)
    limit = request.args.get('limit', 1)
    search = request.args.get('search', None)
    sessions = session.get_sessions(search)
    return make_response(jsonify(get_paginated_list(sessions, url, start, limit)), 200)

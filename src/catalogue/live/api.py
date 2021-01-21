from flask import Blueprint, make_response, jsonify
from flask import request
from . import live
from flask import g

from src.exc.app_exception import MissingFieldException

bp_live = Blueprint('live', 'live')


@bp_live.before_request
def before_request_func():
    # TODO-n: extract user name from the auth
    g.requestor_uuid = 1243242636
    pass


@bp_live.route('/', methods=['POST'])
def create():
    data = request.get_json()
    lives = live.add(data)
    return make_response(jsonify(lives), 201)


@bp_live.route('/', methods=['PUT'])
def update():
    data = request.get_json()
    lives = live.edit(data)
    return make_response(jsonify(lives), 202)


@bp_live.route('/', methods=['GET'])
def get():
    if 'live_uuid' in request.args:
        liveUUID = request.args.get('live_uuid')
        lives = live.get(liveUUID)
        return make_response(jsonify(lives), 200)
    else:
        lives = live.get_lives()
        return make_response(jsonify(lives), 200)


@bp_live.route('/', methods=['DELETE'])
def delete():
    if 'live_uuid' in request.args:
        liveUUID = request.args.get('live_uuid')
        lives = live.delete(liveUUID)
        return make_response(jsonify(lives), 200)
    else:
        raise MissingFieldException('Session ID in the query')

from flask import Blueprint, make_response, jsonify
from flask import request
from . import live
from flask import g

from ...dal.pagination import get_paginated_list

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


@bp_live.route('/<live_uuid>', methods=['PUT'])
def update(live_uuid):
    data = request.get_json()
    updated_live = live.update(live_uuid, data)
    return make_response(jsonify(updated_live), 202)


@bp_live.route('/<live_uuid>', methods=['GET'])
def get_one(live_uuid):
    lives = live.get(live_uuid)
    return make_response(jsonify(lives), 200)


@bp_live.route('/', methods=['GET'])
def get():
    # TODO: filter on the user
    url = request.url
    start = request.args.get('start', 1)
    limit = request.args.get('limit', 1)
    search = request.args.get('search', None)
    lives = live.get_lives(search)
    return make_response(jsonify(get_paginated_list(lives, url, start, limit)), 200)


@bp_live.route('/<live_uuid>', methods=['DELETE'])
def delete(live_uuid):
    lives = live.delete(live_uuid)
    return make_response(jsonify(lives), 200)


@bp_live.route('/user/<user_uuid>', methods=['GET'])
def get_by_user(user_uuid):
    url = request.url
    start = request.args.get('start', 1)
    limit = request.args.get('limit', 1)
    search = request.args.get('search', None)
    lives = live.get_by_user(user_uuid, search)
    return make_response(jsonify(get_paginated_list(lives, url, start, limit)), 200)

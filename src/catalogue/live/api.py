from flask import Blueprint
from flask import request
from . import live


bp_live = Blueprint('live', 'live')


@bp_live.route('/', methods=['POST'])
def create():
    return request.method+' user!'


@bp_live.route('/<uuid>', methods=['GET'])
def get(uuid):
    return request.method+' user!'


@bp_live.route('/<uuid>', methods=['PUT'])
def edit(uuid):
    return request.method+' user!'

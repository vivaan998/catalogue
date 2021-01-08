# Only in this file there should be reference/import to flask.
# TODO-1: Finish/correct the implementation of existing methods and add the new methods if needed
# TODO-1: Perform postman test on the methods exposed here

from flask import Blueprint
from flask import request
from . import session
from flask import g


bp_session = Blueprint('session', 'session')


@bp_session.before_request
def before_request_func():
    # TODO-n: extract user name from the auth
    g.requestor_uuid = 1243242636
    pass


@bp_session.route('/', methods=['POST'])
def create():
    session.create()
    return request.method+' user!'


@bp_session.route('/<uuid>', methods=['GET'])
def get(uuid):
    session.get()
    return request.method+' user!'


@bp_session.route('/<uuid>', methods=['PUT'])
def edit(uuid):
    session.edit()
    return request.method+' user!'

# Only in this file there should be reference/import to flask.
# TODO-1: Finish/correct the implementation of existing methods and add the new methods if needed
# TODO-1: Perform postman test on the methods exposed here

from flask import Blueprint, make_response
from flask import request
from flask import jsonify
from . import image
from flask import g

bp_image = Blueprint('image', 'image')


@bp_image.before_request
def before_request_func():
    # TODO-n: extract user name from the auth
    g.requestor_uuid = 1243242636


@bp_image.route('/', methods=['POST'])
def create():
    images = image.add(request)
    return make_response(jsonify(images), 201)

@bp_image.route('/<session_uuid>', methods=['GET'])
def get(session_uuid):
    images = image.get(session_uuid)
    return make_response(jsonify(images), 200)


@bp_image.route('/<image_uuid>', methods=['DELETE'])
def delete(image_uuid):
    images = image.delete(image_uuid)
    return make_response(jsonify(images), 200)

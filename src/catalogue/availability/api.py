# Only in this file there should be reference/import to flask.
# TODO-1: Finish/correct the implementation of existing methods and add the new methods if needed
# TODO-1: Perform postman test on the methods exposed here

from flask import Blueprint, make_response
from flask import request
from flask import jsonify
from . import availability
from flask import g
from src.exc.app_exception import MissingFieldException

bp_availability = Blueprint('availability', 'availability')


@bp_availability.before_request
def before_request_func():
    # TODO-n: extract user name from the auth
    g.requestor_uuid = 1243242636
    pass


@bp_availability.route('/', methods=['POST'])
def create():
    data = request.get_json()
    availabilities = availability.add(data)
    return make_response(jsonify(availabilities), 201)


@bp_availability.route('/<ref_uuid>', methods=['GET'])
def get(ref_uuid):
    availabilities = availability.get(ref_uuid)
    return make_response(jsonify(availabilities), 200)


@bp_availability.route('/<ref_uuid>/<argument>', methods=['PATCH'])
def patch(ref_uuid, argument):
    if argument == "increase":
        availabilities = availability.increase(ref_uuid)
        if availabilities:
            return get(ref_uuid)
        else:
            return make_response(jsonify("Cannot cancel as there are no booked slots"), 400)

    elif argument == "decrease":
        availabilities = availability.decrease(ref_uuid)
        if availabilities:
            return get(ref_uuid)
        else:
            return make_response(jsonify("All slots are booked"), 400)

    else:
        raise MissingFieldException(' argument for bookings')

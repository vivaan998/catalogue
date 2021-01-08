from flask import Blueprint
from flask import request
from . import image


bp_image = Blueprint('image', 'image')


@bp_image.route('/', methods=['POST'])
def create():
    image.create()
    return request.method+' user!'

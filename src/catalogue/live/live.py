# In this file there should be NO reference/import to flask or SQLAlchemy.
# TODO-1: Finish the implementation of existing methods and add the new methods if needed
# TODO-1: Perform unit test on the methods exposed here

from .core import retrieve_data, delete_data
from src.exc.app_exception import InvalidUUIDException
import datetime
from app import is_valid_uuid


def add(data):
    name = data['name']
    category = data['category']
    hashtags = data['hashtags']
    description = data['description']
    creatorUUID = data['creator_uuid']
    createdTime = datetime.datetime.now()
    lastUpdateDateTime = datetime.datetime.now()
    result = create.write(name, category, hashtags, description, creatorUUID, createdTime, lastUpdateDateTime)
    return result


def edit(data):
    if is_valid_uuid(data['sessionUUID']):
        sessionUUID = data['sessionUUID']
        name = data['name']
        category = data['category']
        hashtags = data['hashtags']
        description = data['description']
        creatorUUID = data['creator_uuid']
        result = update.edit(sessionUUID, name, category, hashtags, description, creatorUUID)
        return result
    else:
        raise InvalidUUIDException('Invalid UUID supplied')


def get(liveUUID):
    # UUID_PATTERN = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)
    if is_valid_uuid(liveUUID):
        live = retrieve_data.read_live(liveUUID)
        return live
    else:
        raise InvalidUUIDException({'error': 'Invalid UUID supplied'})


def delete(liveUUID):
    if is_valid_uuid(liveUUID):
        result = delete_data.delete(liveUUID)
        return result
    else:
        raise InvalidUUIDException({'error': 'Invalid UUID supplied'})


def get_lives():
    lives = retrieve_data.read_lives()
    return lives

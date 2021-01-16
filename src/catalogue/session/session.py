# In this file there should be NO reference/import to flask or SQLAlchemy.
# TODO-1: Finish the implementation of existing methods and add the new methods if needed
# TODO-1: Perform unit test on the methods exposed here

from .core import create, retrieve_data, delete_data, update
from src.exc.app_exception import InvalidUUIDException
import uuid


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


def add(data):
    name = data['name']
    category = data['category']
    hashtags = data['hashtags']
    description = data['description']
    creatorUUID = data['creator_uuid']
    result = create.write(name, category, hashtags, description, creatorUUID)
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
        raise InvalidUUIDException({'error': 'Invalid UUID supplied'})


def get(sessionUUID):
    # UUID_PATTERN = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)
    if is_valid_uuid(sessionUUID):
        sessions = retrieve_data.read_session(sessionUUID)
        return sessions
    else:
        raise InvalidUUIDException({'error': 'Invalid UUID supplied'})


def delete(sessionUUID):
    if is_valid_uuid(sessionUUID):
        result = delete_data.delete(sessionUUID)
        return result
    else:
        raise InvalidUUIDException({'error': 'Invalid UUID supplied'})

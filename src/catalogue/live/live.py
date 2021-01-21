# In this file there should be NO reference/import to flask or SQLAlchemy.
# TODO-1: Finish the implementation of existing methods and add the new methods if needed
# TODO-1: Perform unit test on the methods exposed here

from .core import retrieve_data, delete_data, create, update
from src.exc.app_exception import InvalidUUIDException
import uuid


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


def add(data):
    lives = data['live']
    _from = lives['from']
    _to = lives['to']
    presenter_uuid = lives['presenter_uuid']
    description = lives['description']
    language = lives['language']
    session_uuid = data['session_uuid']
    hashtags = lives['hashtags']
    result = create.write(_from, _to, presenter_uuid, description, language, session_uuid, hashtags)
    return result


def edit(data):
    if is_valid_uuid(data['liveUUID']):
        liveUUID = data['liveUUID']
        lives = data['live']
        _from = lives['from']
        _to = lives['to']
        presenter_uuid = lives['presenter_uuid']
        description = lives['description']
        language = lives['language']
        session_uuid = data['session_uuid']
        hashtags = lives['hashtags']
        result = update.edit(liveUUID, _from, _to, presenter_uuid, description, language, session_uuid, hashtags)
        return result
    else:
        raise InvalidUUIDException({'error': 'Invalid UUID supplied'})


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

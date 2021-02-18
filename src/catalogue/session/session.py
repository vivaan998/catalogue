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
    tokens = data['tokens']
    description = data['description']
    language_iso = data['language_iso']
    creator_uuid = data['creator_uuid']
    result = create.write(name, category, hashtags, tokens, description, language_iso, creator_uuid)
    return result


def edit(session_uuid, data):
    name = data['name']
    tokens = data['tokens']
    category = data['category']
    hashtags = data['hashtags']
    description = data['description']
    language_iso = data['language_iso']
    creator_uuid = data['creator_uuid']
    result = update.edit(session_uuid, name, tokens, category, hashtags, description, language_iso, creator_uuid)
    return result


def get(session_uuid):
    # UUID_PATTERN = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)
    if is_valid_uuid(session_uuid):
        sessions = retrieve_data.read_session(session_uuid)
        return sessions
    else:
        raise InvalidUUIDException('Invalid UUID supplied')


def delete(session_uuid):
    if is_valid_uuid(session_uuid):
        result = delete_data.delete(session_uuid)
        return result
    else:
        raise InvalidUUIDException('Invalid UUID supplied')


def get_sessions(search):
    sessions = retrieve_data.read_sessions(search)
    return sessions


def get_lives(session_uuid, search):
    lives = retrieve_data.read_lives(session_uuid, search)
    return lives

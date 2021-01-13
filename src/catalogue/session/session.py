# In this file there should be NO reference/import to flask or SQLAlchemy.
# TODO-1: Finish the implementation of existing methods and add the new methods if needed
# TODO-1: Perform unit test on the methods exposed here

from .core import create, retrieve_data, delete_data, update
import datetime


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
    sessionUUID = data['sessionUUID']
    name = data['name']
    category = data['category']
    hashtags = data['hashtags']
    description = data['description']
    creatorUUID = data['creator_uuid']
    result = update.edit(sessionUUID, name, category, hashtags, description, creatorUUID)

    return result


def get(sessionUUID):
    sessions = retrieve_data.read_session(sessionUUID)
    return sessions


def delete(sessionUUID):
    result = delete_data.delete(sessionUUID)
    return result

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
    result, code = create.write(name, category, hashtags, description, creatorUUID, createdTime, lastUpdateDateTime)
    return result, code


def edit(data):
    sessionUUID = data['sessionUUID']
    name = data['name']
    category = data['category']
    hashtags = data['hashtags']
    description = data['description']
    creatorUUID = data['creator_uuid']
    createdTime = datetime.datetime.now()
    lastUpdateDateTime = datetime.datetime.now()
    result, code = update.edit(sessionUUID, name, category, hashtags, description, creatorUUID, createdTime, lastUpdateDateTime)

    return result, code


def get(sessionUUID):
    sessions, code = retrieve_data.read_session(sessionUUID) 
    return sessions, code


def delete(sessionUUID):
    result, code = delete_data.delete(sessionUUID)
    return result, code

# In this file there should be NO reference/import to flask or SQLAlchemy.
# TODO-1: Finish the implementation of existing methods and add the new methods if needed
# TODO-1: Perform unit test on the methods exposed here

from .core import retrieve_data, delete_data, create
from .core import update as live_update
from datetime import datetime


def add(data):
    dt_from = datetime.strptime(data['from'], "%Y-%m-%dT%H:%M:%S.%fZ")
    dt_to = datetime.strptime(data['to'], "%Y-%m-%dT%H:%M:%S.%fZ")
    presenter_uuid = data['presenter_uuid']
    description = data['description']
    session_uuid = data['session_uuid']
    hashtags = data.get("hashtags", None)
    result = create.write(dt_from, dt_to, presenter_uuid, description, session_uuid, hashtags)
    return result


def update(live_uuid, data):
    dt_from = datetime.strptime(data['from'], "%Y-%m-%dT%H:%M:%S.%fZ")
    dt_to = datetime.strptime(data['to'], "%Y-%m-%dT%H:%M:%S.%fZ")
    presenter_uuid = data['presenter_uuid']
    description = data['description']
    session_uuid = data['session_uuid']
    hashtags = data.get("hashtags", None)
    result = live_update.edit(live_uuid, dt_from, dt_to, presenter_uuid, description, session_uuid, hashtags)
    return result


def get(liveUUID):
    live = retrieve_data.read_live(liveUUID)
    return live


def delete(liveUUID):
    result = delete_data.delete(liveUUID)
    return result


def get_lives(search):
    lives = retrieve_data.read_lives(search)
    return lives


def get_by_user(user_uuid, search):
    lives = retrieve_data.read_lives_by_users(user_uuid, search)
    return lives

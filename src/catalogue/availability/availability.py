# In this file there should be NO reference/import to flask or SQLAlchemy.
# TODO-1: Finish the implementation of existing methods and add the new methods if needed
# TODO-1: Perform unit test on the methods exposed here

from .core import create, retrieve_data, patch_data


def add(data):
    liveUUID = data['ref_uuid']
    maxSlots = int(data['max_slots'])
    result = create.write(liveUUID, maxSlots)
    return result


def get(liveUUID):
    result = retrieve_data.read_availability(liveUUID)
    return result


def increase(liveUUID):
    result = patch_data.increaseBookSlot(liveUUID)
    return result


def decrease(liveUUID):
    result = patch_data.decreaseBookSlot(liveUUID)
    return result

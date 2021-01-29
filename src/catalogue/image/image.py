# In this file there should be NO reference/import to flask or SQLAlchemy.
# TODO-1: Finish the implementation of existing methods and add the new methods if needed
# TODO-1: Perform unit test on the methods exposed here

from .core import create, retrieve_data, delete_data
from src.exc.app_exception import InvalidUUIDException
import uuid

def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


def add(request):
    image_file = request.files.get('upfile')
    session_uuid = request.form['session_uuid']
    if is_valid_uuid(session_uuid):
        result = create.write(image_file, session_uuid)
        return result
    else:
        raise InvalidUUIDException('Invalid UUID supplied')

def get(session_uuid):
    print('#####', session_uuid)
    if is_valid_uuid(session_uuid):
        images = retrieve_data.read_images(session_uuid)
        return images
    else:
        raise InvalidUUIDException('Invalid UUID supplied')

def delete(image_uuid):
    if is_valid_uuid(image_uuid):
        result = delete_data.delete(image_uuid)
        return result
    else:
        raise InvalidUUIDException('Invalid UUID supplied')


# Only in this file and its sibling / children)
# there should be reference/import to SQLAlchemy/Db().
# NO reference to flask.
# TODO-1: Finish the implementation of existing methods and add the new files / methods if needed

from sqlalchemy.exc import IntegrityError
from src.dal.db import Db
import uuid
import os
from config import basedir
from src.exc.app_exception import ServerException


def _populate_image_model(table_type, session_uuid):
    
    new_uuid = str(uuid.uuid4())
    table = table_type(RefUUID=new_uuid)
    table.SessionUUID = session_uuid
    table.Uri = 'static/' + session_uuid + '/' + new_uuid + '.jpg'
    return table


def write(image_file, session_uuid):
    db_instance = Db()

    image_table = db_instance.model.Image
    sql_image_table = _populate_image_model(image_table, session_uuid)
    session = db_instance.session
    try:
        session.add(sql_image_table)
        session.commit()
        url = os.path.join(basedir, 'static/' + session_uuid)

        if not os.path.exists(url):
            os.makedirs(os.path.join(basedir, 'static/' + session_uuid))
            image_file.save(url + '/' + sql_image_table.RefUUID + '.jpg')
        else:
            image_file.save(url + '/' + sql_image_table.RefUUID + '.jpg')
            
        return {'image_uuid': sql_image_table.RefUUID}

    except IntegrityError as ex:
        print(str(ex))
        session.rollback()
        raise ServerException(str(ex))
    except Exception as ex:
        print(str(ex))
        session.rollback()
        raise ServerException(str(ex))

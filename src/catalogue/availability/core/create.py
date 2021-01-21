# Only in this file and its sibling / children)
# there should be reference/import to SQLAlchemy/Db().
# NO reference to flask.
# TODO-1: Finish the implementation of existing methods and add the new files / methods if needed

from sqlalchemy.exc import IntegrityError
from src.dal.db import Db
from src.exc.app_exception import IntegrityException, ServerException
import datetime


def _populate_avaibility_model(table_type, uuid, maxSlots, bookedSlots, lastUpdateDatetime):
    table = table_type(LiveUUID=uuid)
    table.MaxSlots = maxSlots
    table.BookedSlots = bookedSlots # initially booked slots will 0
    return table


def write(liveUUID, maxSlots):
    db_instance = Db()
    availability_table = db_instance.model.Availability
    sql_avaibility_table = _populate_avaibility_model(availability_table, liveUUID, maxSlots, 0, datetime.datetime.now())
    avaibility = db_instance.session
    try:
        avaibility.add(sql_avaibility_table)
        avaibility.commit()

        return {'liveUUID': sql_avaibility_table.LiveUUID}

    except IntegrityError as ex:
        print(str(ex))
        avaibility.rollback()
        raise IntegrityException({'error': str(ex)})
    except Exception as ex:
        print(str(ex))
        avaibility.rollback()
        raise ServerException({'error': str(ex)})

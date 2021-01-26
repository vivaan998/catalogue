# Only in this file and its sibling / children)
# there should be reference/import to SQLAlchemy/Db().
# NO reference to flask.
# TODO-1: Finish the implementation of existing methods and add the new files / methods if needed

from sqlalchemy.exc import IntegrityError
from src.dal.db import Db
from src.exc.app_exception import IntegrityException, ServerException


def _populate_availability_model(table_type, uuid, max_slots, booked_slots):
    table = table_type(LiveUUID=uuid)
    table.MaxSlots = max_slots
    table.BookedSlots = booked_slots  # initially booked slots will 0
    return table


def write(liveUUID, max_slots):
    db_instance = Db()
    availability_table = db_instance.model.Availability
    sql_availability_table = _populate_availability_model(availability_table, liveUUID, max_slots, 0)
    availability = db_instance.session
    try:
        availability.add(sql_availability_table)
        availability.commit()
        return {'ref_uuid': sql_availability_table.LiveUUID, "max_slots": max_slots}

    except IntegrityError as ex:
        print(str(ex))
        availability.rollback()
        raise IntegrityException(str(ex))
    except Exception as ex:
        print(str(ex))
        availability.rollback()
        raise ServerException(str(ex))

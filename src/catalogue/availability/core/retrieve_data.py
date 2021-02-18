from sqlalchemy.orm import exc
from src.dal.db import Db
from src.exc.app_exception import NotFoundException, ServerException


##
# Fetch availabilities based on UUID
##

def read_availability(liveUUID):
    db_instance = Db()
    availability = db_instance.session
    t_availability = db_instance.model.Availability
    try:
        results = dict()
        availabilities = availability.query(t_availability).filter(t_availability.LiveUUID == liveUUID).one()
        results['live_uuid'] = availabilities.LiveUUID
        results['max_slots'] = availabilities.MaxSlots
        results['booked_slots'] = availabilities.BookedSlots
        return results

    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException(liveUUID + ' Live ID not found')
    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))

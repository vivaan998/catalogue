from sqlalchemy.orm import exc
from src.dal.db import Db
import datetime
from src.exc.app_exception import ServerException, NotFoundException, ConflictException
from .retrieve_data import read_availability


##
# Update available slots based on liveUUID
##

# increaseBookSlot means cancelation of booking
def increaseBookSlot(liveUUID):
    db_instance = Db()
    availability = db_instance.session
    t_availability = db_instance.model.Availability

    try:
        getData = read_availability(liveUUID)
        if getData['max_slots'] < 100:
            lives = availability.query(t_availability).filter(t_availability.LiveUUID == liveUUID).update({
                'MaxSlots': getData['max_slots'] + 1,
                'BookedSlots': getData['booked_slots'] - 1,
                'LastUpdateDatetime': datetime.datetime.now(),
            })
            if lives:
                availability.commit()
                return True
            else:
                raise ConflictException('There are conflicts with the requested Id ' + liveUUID + " in slot booking")
        else:
            return False
    except ConflictException as ex:
        print(str(ex))
        availability.rollback()
        raise ConflictException(str(ex))
    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException(str(ex))
    except Exception as ex:
        print(str(ex))
        availability.rollback()
        raise ServerException(str(ex))


# decreaseBookSlot means cancellation of booking
def decreaseBookSlot(liveUUID):
    db_instance = Db()
    availability = db_instance.session
    t_availability = db_instance.model.Availability
    try:
        getData = read_availability(liveUUID)
        if getData['max_slots'] > 0:
            lives = availability.query(t_availability).filter(t_availability.LiveUUID == liveUUID).update({
                'MaxSlots': getData['max_slots'] - 1,
                'BookedSlots': getData['booked_slots'] + 1,
                'LastUpdateDatetime': datetime.datetime.now(),
            })
            if lives:
                availability.commit()
                return True
            else:
                raise ConflictException('There are conflicts with the requested Id ' + liveUUID + " in slot booking")
        else:
            return False

    except ConflictException as ex:
        print(str(ex))
        availability.rollback()
        raise ConflictException(str(ex))
    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException(str(ex))
    except Exception as ex:
        print(str(ex))
        availability.rollback()
        raise ServerException(str(ex))

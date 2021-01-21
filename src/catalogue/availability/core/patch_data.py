from sqlalchemy.orm import exc
from src.dal.db import Db
import datetime
from src.exc.app_exception import ServerException, NotFoundException
from .retrieve_data import read_avaibility

##
# Update live based on UUID
##

#increaseBookSlot means cancelation of booking
def increaseBookSlot(liveUUID):
    db_instance = Db()
    avaibilty = db_instance.session
    t_avaibility = db_instance.model.Availability

    try:
        getData = read_avaibility(liveUUID)
        if getData['max_slots'] < 100:
            lives = avaibilty.query(t_avaibility).filter(t_avaibility.LiveUUID == liveUUID).update({
                    'MaxSlots': getData['max_slots'] + 1,
                    'BookedSlots': getData['booked_slots'] - 1,
                    'LastUpdateDatetime': datetime.datetime.now(),
                })
            avaibilty.commit()
            return True
        else:
            return False


    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException({'error': str(ex)})
    except Exception as ex:
        print(str(ex))
        avaibilty.rollback()
        raise ServerException({'error': str(ex)})

#decreaseBookSlot means cancelation of booking
def decreaseBookSlot(liveUUID):
    db_instance = Db()
    avaibilty = db_instance.session
    t_avaibility = db_instance.model.Availability
    try:
        getData = read_avaibility(liveUUID)
        if getData['max_slots'] > 0:
            lives = avaibilty.query(t_avaibility).filter(t_avaibility.LiveUUID == liveUUID).update({
                    'MaxSlots': getData['max_slots'] - 1,
                    'BookedSlots': getData['booked_slots'] + 1,
                    'LastUpdateDatetime': datetime.datetime.now(),
                })
            avaibilty.commit()
            return True
        else:
            return False


    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException({'error': str(ex)})
    except Exception as ex:
        print(str(ex))
        avaibilty.rollback()
        raise ServerException({'error': str(ex)})

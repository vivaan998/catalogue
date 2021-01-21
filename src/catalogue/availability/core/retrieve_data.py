from sqlalchemy.orm import exc
from src.dal.db import Db
from src.exc.app_exception import NotFoundException, ServerException


##
# Fetch Session based on UUID
##

def read_avaibility(liveUUID):
    db_instance = Db()
    avaibility = db_instance.session
    t_avaibility = db_instance.model.Availability
    try:
        results = dict()
        avaibilities = avaibility.query(t_avaibility).filter(t_avaibility.LiveUUID == liveUUID).one()
        results['ref_uuid'] = avaibilities.LiveUUID
        results['max_slots'] = avaibilities.MaxSlots
        results['booked_slots'] = avaibilities.BookedSlots
        return results

    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException({'error': str(ex)})

    except Exception as ex:
        print(str(ex))
        raise ServerException({'error': str(ex)})

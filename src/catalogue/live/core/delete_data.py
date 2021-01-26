from sqlalchemy.orm import exc
from src.dal.db import Db
from src.exc.app_exception import NotFoundException, ServerException


##
# Delete based on live UUID
##

def delete(liveUUID):
    db_instance = Db()
    session = db_instance.session
    t_live = db_instance.model.Live
    try:
        live = session.query(t_live).filter(t_live.UUID == liveUUID).delete()
        session.commit()
        if live:
            return 'Live deleted'
        else:
            raise NotFoundException('Live UUID ' + liveUUID + " not found")

    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))

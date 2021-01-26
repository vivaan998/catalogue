from sqlalchemy.orm import exc
from src.dal.db import Db
from src.exc.app_exception import NotFoundException, ServerException


##
# Delete Session based on UUID
##

def delete(sessionUUID):
    db_instance = Db()
    session = db_instance.session
    t_session = db_instance.model.Session
    try:
        sessions = session.query(t_session).filter(t_session.UUID == sessionUUID).delete()
        session.commit()
        if sessions:
            return 'Successfully deleted'
        else:
            raise NotFoundException('Session UUID ' + sessionUUID + " not found")
    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))

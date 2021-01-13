from sqlalchemy.orm import exc
from src.dal.db import Db
from src.exc.app_exception import NotFoundException, ServerException


##
# ALL Categories based on language
##

def delete(sessionUUID):
    db_instance = Db()
    session = db_instance.session
    t_session = db_instance.model.Session
    try:
        sessions = session.query(t_session).filter(t_session.UUID == sessionUUID).delete()
        session.commit()
        if sessions:
            return {'check': 'deleted'}

    except exc.NoResultFound as ex:
        print(str(ex))
        return NotFoundException(str(ex))
    except Exception as ex:
        print(str(ex))
        return ServerException(str(ex))

from sqlalchemy.orm import exc
from src.dal.db import Db
from ....exception.SessionException import NotFound, GeneralException



##
# ALL Categories based on language
##

def delete(sessionUUID):
    db_instance = Db()
    session = db_instance.session
    t_session = db_instance.model.Session
    sessions = None
    try:
        sessions = session.query(t_session).filter(t_session.UUID == sessionUUID).delete()
        session.commit()

    except exc.NoResultFound as ex:
        print(str(ex))
        return NotFound(sessionUUID, ex), 404
    
    except Exception as ex:
        print(str(ex))
        return GeneralException(ex), 403

    if not sessions:
        return NotFound(sessionUUID, exc.NoResultFound), 404
    else:
        return {'check': 'deleted'}, 204

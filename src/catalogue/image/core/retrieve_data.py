from sqlalchemy.orm import exc, Load
from sqlalchemy import or_
from src.dal.db import Db
from src.exc.app_exception import NotFoundException, ServerException
from sqlalchemy.orm import joinedload


##
# Fetch Session based on UUID
##

def read_session(sessionUUID):
    db_instance = Db()
    session = db_instance.session
    t_image = db_instance.model.Image
    try:
        temp = []
        query = session.query(t_image).filter(t_image.SessionUUID == sessionUUID).all()
        for i in query:
            temp.append({
                "uuid": i.RefUUID,
                "uri": i.Uri,
                "session_uuid": i.SessionUUID
            })
        return temp

    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException('Session Id ' + sessionUUID + " not found")
    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))



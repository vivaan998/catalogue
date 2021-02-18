from sqlalchemy.orm import exc, Load
from sqlalchemy import or_
from src.dal.db import Db
from src.exc.app_exception import NotFoundException, ServerException
from sqlalchemy.orm import joinedload


##
# Fetch Image based on UUID
##

def read_images(sessionUUID):

    db_instance = Db()
    session = db_instance.session
    t_image = db_instance.model.Image
    try:
        result = []
        query = session.query(t_image).filter(t_image.SessionUUID == sessionUUID).all()
        for image in query:
            result.append({
                "uuid": image.RefUUID,
                "uri": image.Uri,
                "session_uuid": image.SessionUUID
            })
        return result

    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException('Session Id ' + sessionUUID + " not found")
    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))



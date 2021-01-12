from sqlalchemy.orm import exc
from src.dal.db import Db
from ....exception.SessionException import NotFound, GeneralException


##
# ALL Categories based on language
##

def read_session(sessionUUID):
    db_instance = Db()
    session = db_instance.session
    t_session = db_instance.model.Session
    t_sessionTag = db_instance.model.SessionTag
    sessions = None
    try:
        results = dict()
        sessions = session.query(t_session).filter(t_session.UUID == sessionUUID).one()
        hashtags = session.query(t_sessionTag).filter(t_sessionTag.SessionUUID == sessionUUID).one()
        results['name'] = sessions.Name
        results['category'] = {
            'value': sessions.Category,
            'uuid' : sessions.UUID
        }
        results['hashtags'] = (hashtags.Hashtag).split(',')
        results['description'] = {
            'value' : sessions.Description,
            'code'  : sessions.LanguageISO
        }
        results['created_uuid'] = sessions.CreatorUUID
        results['tokens'] = 0
        results['uuid'] = sessions.UUID
        results['created_at'] = sessions.CreationDateTime
    
    except exc.NoResultFound as ex:
        print(str(ex))
        return NotFound(sessionUUID, ex), 404

    except Exception as ex:
        print(str(ex))
        return GeneralException(ex), 403

    
    return results, 200

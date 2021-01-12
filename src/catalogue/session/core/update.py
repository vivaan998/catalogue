from sqlalchemy.orm import exc
from src.dal.db import Db
import datetime
from ....exception.SessionException import NotFound, GeneralException
##
# ALL Categories based on language
##

def edit(sessionUUID, name, category, hashtags, description, creatorUUID, createdTime, lastUpdateDateTime):
    db_instance = Db()
    session = db_instance.session
    t_session = db_instance.model.Session
    t_sessionTag = db_instance.model.SessionTag

    sessions = None
    hashSessions = None
    try:
        sessions = session.query(t_session).filter(t_session.UUID == sessionUUID).update({
            'Name' : name,
            'Category' : category['value'],
            'LastUpdateDatetime' : datetime.datetime.now(),
            'LanguageISO' : description['code'],
            'Description' : description['value'],
 
        })

        hashSessions = session.query(t_sessionTag).filter(t_sessionTag.SessionUUID == sessionUUID).update({
            'Hashtag' : ','.join(hashtags),
            'LanguageISO' : description['code']
        })        

        session.commit()

    except exc.NoResultFound as ex:
        print(str(ex))
        return NotFound(sessionUUID, ex)
    
    except Exception as ex:
        print(str(ex))
        session.rollback()
        return GeneralException(ex), 403

    if sessions: 
        return {'info' : 'Successfuly updated for UUID: ' + sessionUUID}, 200
    else:
        return GeneralException(ex), 403
from sqlalchemy.orm import exc
from src.dal.db import Db
import datetime
from src.exc.app_exception import ServerException, NotFoundException


##
# Update Session based on UUID
##

def edit(sessionUUID, name, category, hashtags, description, creatorUUID):
    db_instance = Db()
    session = db_instance.session
    t_session = db_instance.model.Session
    t_sessionTag = db_instance.model.SessionTag

    try:
        sessions = session.query(t_session).filter(t_session.UUID == sessionUUID,
                                                   t_session.CreatorUUID == creatorUUID).update(
            {
                'Name': name,
                'Category': category['value'],
                'LastUpdateDatetime': datetime.datetime.now(),
                'LanguageISO': description['code'],
                'Description': description['value'],
            })

        hashSessions = session.query(t_sessionTag).filter(t_sessionTag.SessionUUID == sessionUUID).update({
            'Hashtag': ','.join(hashtags),
            'LanguageISO': description['code']
        })

        session.commit()

        if sessions and hashSessions:
            return {'session_uuid': sessionUUID + ' successfully updated'}

    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException({'error': str(ex)})
    except Exception as ex:
        print(str(ex))
        session.rollback()
        raise ServerException({'error': str(ex)})

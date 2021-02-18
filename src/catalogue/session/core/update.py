from sqlalchemy.orm import exc
from src.dal.db import Db
import datetime
from src.exc.app_exception import ServerException, NotFoundException, ConflictException


##
# Update Session based on UUID
##

def edit(sessionUUID, name, tokens, category, hashtags, description, LanguageISO, creatorUUID):
    db_instance = Db()
    session = db_instance.session
    t_session = db_instance.model.Session
    t_sessionTag = db_instance.model.SessionTag
    try:
        sessions = session.query(t_session).filter(t_session.UUID == sessionUUID,
                                                   t_session.CreatorUUID == creatorUUID).update(
            {
                'Name': name,
                'Tokens': tokens,
                'Category': category['uuid'],
                'LastUpdateDatetime': datetime.datetime.now(),
                'LanguageISO': LanguageISO,
                'Description': description,
            })

        hashSessions = session.query(t_sessionTag).filter(t_sessionTag.SessionUUID == sessionUUID).update({
            'Hashtag': ','.join(hashtags) if len(hashtags) > 0 else '',
            'LanguageISO': LanguageISO if LanguageISO != '' else 'en'
        })

        if sessions and hashSessions:
            session.commit()
            return 'Session updated'
        else:
            raise ConflictException('There are conflicts with the requested Id ' + sessionUUID)
    except ConflictException as ex:
        print(str(ex))
        session.rollback()
        raise ConflictException(str(ex))
    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException(str(ex))
    except Exception as ex:
        print(str(ex))
        session.rollback()
        raise ServerException(str(ex))

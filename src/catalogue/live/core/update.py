from sqlalchemy.orm import exc
from src.dal.db import Db
import datetime
from src.exc.app_exception import ServerException, NotFoundException, ConflictException


##
# Update live based on UUID
##

def edit(liveUUID, dt_from, dt_to, presenter_uuid, description, session_uuid, hashtags):
    db_instance = Db()
    session = db_instance.session
    t_live = db_instance.model.Live
    t_liveTag = db_instance.model.LiveTag
    session_table = db_instance.model.Session
    try:
        language = session.query(session_table).filter(session_table.UUID == session_uuid).one().LanguageISO
    except exc.NoResultFound as ex:
        print(ex)
        raise NotFoundException('No such session found with UUID: ' + session_uuid)
    try:
        lives = session.query(t_live).filter(t_live.UUID == liveUUID).update({
                'StartAtGMT': dt_from,
                'EndsAtGMT': dt_to,
                'PresenterUUID': presenter_uuid,
                'SessionUUID': session_uuid,
                'LanguageISO': language,
                'Description': description,
                'LastUpdateDatetime': datetime.datetime.now(),
            })

        hashLives = session.query(t_liveTag).filter(t_liveTag.LiveUUID == liveUUID).update({
            'Hashtag': ','.join(hashtags) if hashtags is not None else '',
            'LanguageISO': language
        })

        if lives and hashLives:
            session.commit()
            return 'Live updated'
        else:
            raise ConflictException('There are conflicts with the requested Id ' + liveUUID)

    except ConflictException as ex:
        print(str(ex))
        session.rollback()
        raise ConflictException(str(ex))
    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException('No such live found with UUID: ' + liveUUID)
    except Exception as ex:
        print(str(ex))
        session.rollback()
        raise ServerException(str(ex))

from sqlalchemy.orm import exc
from src.dal.db import Db
import datetime
from src.exc.app_exception import ServerException, NotFoundException


##
# Update live based on UUID
##

def edit(liveUUID, _from, _to, presenter_uuid, description, language, session_uuid, hashtags):
    db_instance = Db()
    session = db_instance.session
    t_live = db_instance.model.Live
    t_liveTag = db_instance.model.LiveTag

    try:
        lives = session.query(t_live).filter(t_live.UUID == liveUUID).update({
                'StartAtGMT': _from,
                'EndsAtGMT': _to,
                'PresenterUUID': presenter_uuid,
                'SessionUUID': session_uuid,
                'LanguageISO': language,
                'Description': description,
                'LastUpdateDatetime': datetime.datetime.now(),
            })

        hashLives = session.query(t_liveTag).filter(t_liveTag.LiveUUID == liveUUID).update({
            'Hashtag': ','.join(hashtags),
            'LanguageISO': language
        })

        session.commit()

        if lives and hashLives:
            return {'live_uuid': liveUUID + ' successfully updated'}

    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException({'error': str(ex)})
    except Exception as ex:
        print(str(ex))
        session.rollback()
        raise ServerException({'error': str(ex)})

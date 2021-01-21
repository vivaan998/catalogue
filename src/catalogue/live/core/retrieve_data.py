from sqlalchemy.orm import exc
from src.dal.db import Db
from src.exc.app_exception import NotFoundException, ServerException


##
# ALL Lives and live based on LiveUUID
##

def read_live(liveUUID):
    db_instance = Db()
    session = db_instance.session
    t_live = db_instance.model.Live
    t_liveTag = db_instance.model.LiveTag
    t_session = db_instance.model.Session
    try:
        results = dict()
        lives = session.query(t_live).filter(t_live.UUID == liveUUID).one()
        hashtags = session.query(t_liveTag).filter(t_liveTag.LiveUUID == liveUUID).one()
        sessions = session.query(t_session).filter(t_session.UUID == lives.SessionUUID).one()
        results['from'] = lives.StartAtGMT
        results['to'] = lives.EndsAtGMT
        results['hashtags'] = hashtags.Hashtag.split(',')
        results['description'] = lives.Description
        results['uuid'] = lives.UUID
        results['language'] = lives.LanguageISO
        results['session_uuid'] = sessions.UUID
        results['streaming_uuid'] = 'ASK'
        return results

    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException('Live Id ' + liveUUID + " not found")
    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))


def read_lives():
    db_instance = Db()
    session = db_instance.session
    t_live = db_instance.model.Live
    t_liveTag = db_instance.model.LiveTag
    t_session = db_instance.model.Session
    try:
        results = []
        lives = session.query(t_live).all()
        if lives:
            for live in lives:
                hashtags = session.query(t_liveTag).filter(t_liveTag.LiveUUID == live.UUID).one()
                sessions = session.query(t_session).filter(t_session.UUID == live.SessionUUID).one()
                result = {
                            'from': live.StartAtGMT,
                            'to': live.EndsAtGMT,
                            'hashtags': hashtags.Hashtag.split(','),
                            'description': live.Description,
                            'uuid': live.UUID,
                            'language': live.LanguageISO,
                            'session_uuid': sessions.UUID,
                            'streaming_uuid': 'ASK'
                        }
                results.append(result)
        return results

    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))

from sqlalchemy import or_
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
    try:
        lives = session.query(t_live).filter(t_live.UUID == liveUUID).one()
    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException('Live Id ' + liveUUID + " not found")
    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))

    try:
        hashtags = session.query(t_liveTag).filter(t_liveTag.LiveUUID == liveUUID).one()
    except exc.NoResultFound as ex:
        print(str(ex))
        hashtags = None
        pass
    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))        

    results = dict()
    results['from'] = lives.StartAtGMT.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    results['to'] = lives.EndsAtGMT.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    results['hashtags'] = hashtags.Hashtag.split(',') if hashtags.Hashtag != '' else []
    results['description'] = lives.Description
    results['uuid'] = lives.UUID
    results['language'] = lives.LanguageISO
    results['session_uuid'] = lives.SessionUUID
    results['presenter_uuid'] = lives.PresenterUUID
    return results


def read_lives(search):
    db_instance = Db()
    session = db_instance.session
    t_live = db_instance.model.Live
    t_liveTag = db_instance.model.LiveTag
    try:
        results = []
        if search is None:
            lives = session.query(t_live).all()
        else:
            lives = session.query(t_live).filter(or_(t_live.Description.contains(search)))
        if lives:
            for live in lives:
                hashtags = session.query(t_liveTag).filter(t_liveTag.LiveUUID == live.UUID).one()
                result = {
                            'from': live.StartAtGMT.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                            'to': live.EndsAtGMT.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                            'hashtags': hashtags.Hashtag.split(',') if hashtags.Hashtag != '' else [],
                            'description': live.Description,
                            'uuid': live.UUID,
                            'language': live.LanguageISO,
                            'session_uuid': live.SessionUUID,
                        }
                results.append(result)
        return results

    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))

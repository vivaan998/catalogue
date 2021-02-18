from sqlalchemy import or_, and_
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
    t_live_tag = db_instance.model.LiveTag
    try:
        query = session.query(t_live).join(t_live_tag)
        lives = query.filter(t_live.UUID == liveUUID).one()
        hashtags = lives.LiveTag
    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException('Live Id ' + liveUUID + " not found")
    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))

    results = dict()
    results['from'] = lives.StartAtGMT.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    results['to'] = lives.EndsAtGMT.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    results['hashtags'] = hashtags[0].Hashtag.split(',') if hashtags[0].Hashtag != '' else []
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
    t_live_tag = db_instance.model.LiveTag
    t_session = db_instance.model.Session
    try:
        results = []
        query = session.query(t_live).join(t_live_tag)
        if search is None:
            lives = query.all()
        else:
            lives = query.filter(or_(t_live.Description.contains(search), t_live_tag.Hashtag.contains(search),
                                     and_(or_(t_session.Name.contains(search), t_session.Description.contains(search)),
                                          t_session.UUID == t_live.SessionUUID)))
        if lives:
            for live in lives:
                hashtags = live.LiveTag
                result = {
                    'from': live.StartAtGMT.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    'to': live.EndsAtGMT.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    'hashtags': hashtags[0].Hashtag.split(',') if hashtags[0].Hashtag != '' else [],
                    'description': live.Description,
                    'presenter_uuid': live.PresenterUUID,
                    'uuid': live.UUID,
                    'language': live.LanguageISO,
                    'session_uuid': live.SessionUUID,
                }
                results.append(result)
        return results

    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))


def read_lives_by_users(user_uuid, search):
    db_instance = Db()
    session = db_instance.session
    t_live = db_instance.model.Live
    t_live_tag = db_instance.model.LiveTag
    t_session = db_instance.model.Session
    try:
        results = []
        query = session.query(t_live).join(t_live_tag)
        if search is None:
            lives = query.filter(or_(t_live.PresenterUUID == user_uuid, t_session.CreatorUUID == user_uuid))
        else:
            lives = query.filter(or_(t_live.PresenterUUID == user_uuid, t_session.CreatorUUID == user_uuid),
                                 or_(t_session.Name.contains(search), t_session.Description.contains(search)),
                                 t_session.UUID == t_live.SessionUUID)
        if lives:
            for live in lives:
                hashtags = live.LiveTag
                result = {
                    'from': live.StartAtGMT.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    'to': live.EndsAtGMT.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                    'hashtags': hashtags[0].Hashtag.split(',') if hashtags[0].Hashtag != '' else [],
                    'description': live.Description,
                    'uuid': live.UUID,
                    'language': live.LanguageISO,
                    'presenter_uuid': live.PresenterUUID,
                    'session_uuid': live.SessionUUID,
                }
                results.append(result)
        return results

    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))

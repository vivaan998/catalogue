from sqlalchemy.orm import exc
from sqlalchemy import or_, and_
from src.dal.db import Db
from src.exc.app_exception import NotFoundException, ServerException


##
# Fetch Session based on UUID
##

def read_session(sessionUUID):
    db_instance = Db()
    session = db_instance.session
    t_session = db_instance.model.Session
    t_session_tag = db_instance.model.SessionTag
    t_category = db_instance.model.Categories
    try:
        query = session.query(t_session).join(t_session_tag).join(t_category)
        results = dict()
        sessions = query.filter(t_session.UUID == sessionUUID).one()
        hashtags = sessions.SessionTag
        category = sessions.Categories
        results['name'] = sessions.Name
        results['category'] = {
            'value': category.Value,
            'UUID': category.UUID
        }
        results['hashtags'] = hashtags[0].Hashtag.split(',') if len(hashtags[0].Hashtag) > 0 else ''
        results['description'] = sessions.Description
        results['language_iso'] = sessions.LanguageISO
        results['creator_uuid'] = sessions.CreatorUUID
        results['tokens'] = sessions.Tokens
        results['uuid'] = sessions.UUID
        results['created_at'] = sessions.CreationDateTime.strftime("%Y-%m-%dT%H:%M:%SZ")
        return results

    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException('Session Id ' + sessionUUID + " not found")
    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))


def read_sessions(search):
    db_instance = Db()
    session = db_instance.session
    t_session = db_instance.model.Session
    t_session_tag = db_instance.model.SessionTag
    t_category = db_instance.model.Categories
    try:
        results = []
        query = session.query(t_session).join(t_session_tag).join(t_category)
        if search is None:
            sessions = query.all()
        else:
            sessions = query.filter(or_(t_session.Name.contains(search), t_session.Description.contains(search),
                                        t_session_tag.Hashtag.contains(search)))
        if sessions:
            for each_session in sessions:
                hashtags = each_session.SessionTag
                category = each_session.Categories
                result = {
                    'name': each_session.Name,
                    'category': {"value": category.Value, "UUID": category.UUID},
                    'hashtags': hashtags[0].Hashtag.split(',') if len(hashtags[0].Hashtag) > 0 else '',
                    'description': each_session.Description,
                    'language_is': each_session.LanguageISO,
                    'creator_uuid': each_session.CreatorUUID,
                    'tokens': each_session.Tokens,
                    'session_uuid': each_session.UUID,
                    'created_at': each_session.CreationDateTime.strftime("%Y-%m-%dT%H:%M:%SZ")
                }
                results.append(result)
        return results
    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))


def read_lives(session_uuid, search):
    db_instance = Db()
    session = db_instance.session
    t_live = db_instance.model.Live
    t_live_tag = db_instance.model.LiveTag
    t_session = db_instance.model.Session
    try:
        results = []
        query = session.query(t_live).join(t_live_tag)
        if search is None:
            lives = query.filter(t_live.SessionUUID == session_uuid)
        else:
            lives = query.filter(t_live.SessionUUID == session_uuid, or_(t_live.Description.contains(search),
                                                                         t_live_tag.Hashtag.contains(search),
                                                                         and_(or_(t_session.Name.contains(search),
                                                                                  t_session.Description.contains(
                                                                                      search)),
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

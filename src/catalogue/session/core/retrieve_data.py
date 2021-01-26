from sqlalchemy.orm import exc
from sqlalchemy import or_
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
        results = dict()
        sessions = session.query(t_session).filter(t_session.UUID == sessionUUID).one()
        hashtags = session.query(t_session_tag).filter(t_session_tag.SessionUUID == sessionUUID).one()
        category = session.query(t_category).filter(t_category.UUID == sessions.Category).one()
        results['name'] = sessions.Name
        results['category'] = {
            'value': category.Value,
            'UUID': category.UUID
        }
        results['hashtags'] = hashtags.Hashtag.split(',') if len(hashtags.Hashtag) > 0 else ''
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
        if search is None:
            sessions = session.query(t_session).all()
        else:
            sessions = session.query(t_session).filter(or_(t_session.Name.contains(search),
                                                           t_session.Description.contains(search)))
        if sessions:
            for each_session in sessions:
                hashtags = session.query(t_session_tag).filter(t_session_tag.SessionUUID == each_session.UUID).one()
                category = session.query(t_category).filter(t_category.UUID == each_session.Category).one()
                result = {
                    'name': each_session.Name,
                    'category': {"value": category.Value, "UUID": category.UUID},
                    'hashtags': hashtags.Hashtag.split(',') if len(hashtags.Hashtag) > 0 else '',
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

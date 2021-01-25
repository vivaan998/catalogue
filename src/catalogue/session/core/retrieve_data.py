from sqlalchemy.orm import exc
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
        results['hashtags'] = hashtags.Hashtag.split(',')
        results['description'] = {
            'value': sessions.Description,
            'code': sessions.LanguageISO
        }
        results['created_uuid'] = sessions.CreatorUUID
        results['tokens'] = 0
        results['uuid'] = sessions.UUID
        results['created_at'] = sessions.CreationDateTime
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
        sessions = session.query(t_session).all()
        if sessions:
            for each_session in sessions:
                hashtags = session.query(t_session_tag).filter(t_session_tag.SessionUUID == each_session.UUID).one()
                category = session.query(t_category).filter(t_category.UUID == each_session.Category).one()
                if search is None:
                    result = {
                        'name': each_session.Name,
                        'category': {"value": category.Value, "UUID": category.UUID},
                        'hashtags': hashtags.Hashtag.split(','),
                        'description': {"value": each_session.Description, "code": each_session.LanguageISO},
                        'creator_uuid': each_session.CreatorUUID,
                        'tokens': 0,
                        'session_uuid': each_session.UUID,
                        'created_at': each_session.CreationDateTime
                    }
                    results.append(result)
                else:
                    if search in each_session.Name or search in category.Value or search in hashtags or search in \
                            each_session.Description:

                        result = {
                            'name': each_session.Name,
                            'category': {"value": category.Value, "UUID": category.UUID},
                            'hashtags': hashtags.Hashtag.split(','),
                            'description': {"value": each_session.Description, "code": each_session.LanguageISO},
                            'creator_uuid': each_session.CreatorUUID,
                            'tokens': 0,
                            'session_uuid': each_session.UUID,
                            'created_at': each_session.CreationDateTime
                        }
                        results.append(result)
        return results

    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))

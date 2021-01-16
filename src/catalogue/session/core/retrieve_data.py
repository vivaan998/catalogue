from sqlalchemy.orm import exc
from src.dal.db import Db
from src.exc.app_exception import NotFoundException, ServerException


##
# ALL Categories based on language
##

def read_session(sessionUUID):
    db_instance = Db()
    session = db_instance.session
    t_session = db_instance.model.Session
    t_sessionTag = db_instance.model.SessionTag
    t_category = db_instance.model.Categories
    try:
        results = dict()
        sessions = session.query(t_session).filter(t_session.UUID == sessionUUID).one()
        hashtags = session.query(t_sessionTag).filter(t_sessionTag.SessionUUID == sessionUUID).one()
        category = session.query(t_category).filter(t_category.UUID == sessions.Category).one()
        results['name'] = sessions.Name
        results['category'] = {
            'value': category.Value,
            'uuid': category.UUID
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
        raise NotFoundException({'error': str(ex)})

    except Exception as ex:
        print(str(ex))
        raise ServerException({'error': str(ex)})

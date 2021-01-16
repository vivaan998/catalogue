# Only in this file and its sibling / children)
# there should be reference/import to SQLAlchemy/Db().
# NO reference to flask.
# TODO-1: Finish the implementation of existing methods and add the new files / methods if needed

from sqlalchemy.exc import IntegrityError
from src.dal.db import Db
import uuid
from src.exc.app_exception import IntegrityException, ServerException


def _populate_live_model(table_type, _from, _to, presenter_uuid, description, language, session_uuid):
    new_uuid = str(uuid.uuid4())
    table = table_type(UUID=new_uuid)
    table.StartAtGMT = _from
    table.EndsAtGMT = _to
    table.PresenterUUID = presenter_uuid
    table.SessionUUID = session_uuid
    table.Description = description
    table.LanguageISO = language
    return table


def _populate_liveTag_model(table_type, live_UUID, hashtags, languageISO):
    table = table_type(LiveUUID=live_UUID)
    table.Hashtag = ','.join(hashtags)
    table.LanguageISO = languageISO
    return table


def writeToLiveTag(live_UUID, hashtags, languageISO):
    db_instance = Db()
    liveTag_table = db_instance.model.LiveTag
    sql_liveTag_table = _populate_liveTag_model(liveTag_table, live_UUID, hashtags, languageISO)
    liveTag = db_instance.session
    try:
        liveTag.add(sql_liveTag_table)
        liveTag.commit()
        return True

    except IntegrityError as ex:
        print(str(ex))
        liveTag.rollback()
        raise IntegrityException({'error': str(ex)})
    except Exception as ex:
        print(str(ex))
        liveTag.rollback()
        raise ServerException({'error': str(ex)})


def write(_from, _to, presenter_uuid, description, language, session_uuid, hashtags):
    db_instance = Db()
    live_table = db_instance.model.Live
    sql_live_table = _populate_live_model(live_table, _from, _to, presenter_uuid, description,
                                          language, session_uuid)
    session = db_instance.session
    try:
        session.add(sql_live_table)
        session.commit()
        insertToLiveTag = writeToLiveTag(sql_live_table.UUID, hashtags, language)
        if insertToLiveTag:
            return {'live_uuid': sql_live_table.UUID}

    except IntegrityError as ex:
        print(str(ex))
        session.rollback()
        raise IntegrityException({'error': str(ex)})
    except Exception as ex:
        print(str(ex))
        session.rollback()
        raise ServerException({'error': str(ex)})

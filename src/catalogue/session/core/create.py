# Only in this file and its sibling / children)
# there should be reference/import to SQLAlchemy/Db().
# NO reference to flask.
# TODO-1: Finish the implementation of existing methods and add the new files / methods if needed

from sqlalchemy.exc import IntegrityError
from src.dal.db import Db
import uuid
from src.exc.app_exception import ServerException


def _populate_session_model(table_type, name, tokens, category, creator_uuid, description, language_iso):
    new_uuid = str(uuid.uuid4())
    table = table_type(UUID=new_uuid)
    table.Tokens = tokens
    table.Name = name
    table.Category = category
    table.CreatorUUID = creator_uuid
    table.Description = description
    table.LanguageISO = language_iso
    return table


def _populate_session_tag_model(table_type, session_UUID, hashtags, languageISO):
    table = table_type(SessionUUID=session_UUID)
    table.Hashtag = ','.join(hashtags) if len(hashtags) > 0 else ''
    if languageISO != '':
        table.LanguageISO = languageISO

    return table


def write_to_session_tag(session_UUID, hashtags, languageISO):
    db_instance = Db()
    sessionTag_table = db_instance.model.SessionTag
    sql_sessionTag_table = _populate_session_tag_model(sessionTag_table, session_UUID, hashtags, languageISO)
    sessionTag = db_instance.session
    try:
        sessionTag.add(sql_sessionTag_table)
        sessionTag.commit()

    except IntegrityError as ex:
        print(str(ex))
        sessionTag.rollback()
        raise ServerException(str(ex))
    except Exception as ex:
        print(str(ex))
        sessionTag.rollback()
        raise ServerException(str(ex))


def write(name, category, hashtags, tokens, description, language_iso, creator_uuid):
    db_instance = Db()
    session_table = db_instance.model.Session
    sql_session_table = _populate_session_model(session_table, name, tokens, category['uuid'], creator_uuid,
                                                description, language_iso)
    session = db_instance.session
    try:
        session.add(sql_session_table)
        session.commit()
        write_to_session_tag(sql_session_table.UUID, hashtags, language_iso)
        return {'session_uuid': sql_session_table.UUID}

    except IntegrityError as ex:
        print(str(ex))
        session.rollback()
        raise ServerException(str(ex))
    except Exception as ex:
        print(str(ex))
        session.rollback()
        raise ServerException(str(ex))

# Only in this file and its sibling / children)
# there should be reference/import to SQLAlchemy/Db().
# NO reference to flask.
# TODO-1: Finish the implementation of existing methods and add the new files / methods if needed

from sqlalchemy.orm import exc
from sqlalchemy.exc import IntegrityError
from src.dal.db import Db
import uuid
from ....exception.SessionException import NotFound, GeneralException

def _populate_session_model(table_type, name, category, creatorUUID, createdTime, lastUpdateDateTime, description, languageISO):
    new_uuid = str(uuid.uuid4())
    table = table_type(UUID=new_uuid)
    table.Name = name
    table.Category = category
    table.CreatorUUID = creatorUUID
    table.CreationDateTime = createdTime
    table.LastUpdateDatetime = lastUpdateDateTime
    table.Description = description
    table.LanguageISO = languageISO
    return table

def _populate_sessionTag_model(table_type, session_UUID, hashtags, languageISO):
    table = table_type(SessionUUID=session_UUID)
    table.Hashtag = ','.join(hashtags)
    table.LanguageISO = languageISO
    return table

# def _populate_sessionTranslation_model(table_type, session_UUID, languageISO, field, value):
#     table = table_type(SessionUUID=session_UUID)
#     table.LanguageISO = languageISO
#     table.Field = field
#     table.Value = value
#     return table

def writeToSessionTag(session_UUID, hashtags, languageISO):
    db_instance = Db()
    sessionTag_table = db_instance.model.SessionTag
    sql_sessionTag_table = _populate_sessionTag_model(sessionTag_table, session_UUID, hashtags, languageISO)
    sessionTag = db_instance.session
    try:
        sessionTag.add(sql_sessionTag_table)
        sessionTag.commit()

    except IntegrityError as ex:
        print(str(ex))
        sessionTag.rollback()
        return False

    except Exception as ex:
        print(str(ex))
        sessionTag.rollback()
        return False

    return True


# def writeToSessionTranslation(session_UUID, languageISO, field, value):
#     db_instance = Db()
#     sessionTranslation_table = db_instance.model.SessionTranslation
#     sql_sessionTranslation_table = _populate_sessionTranslation_model(sessionTranslation_table, session_UUID, languageISO, field, value)
#     sessionTag = db_instance.session
#     try:
#         sessionTag.add(sql_sessionTranslation_table)
#         sessionTag.commit()

#     except IntegrityError as ex:
#         print(str(ex))
#         sessionTag.rollback()
#         return False

#     except Exception as ex:
#         print(str(ex))
#         sessionTag.rollback()
#         return False

#     return True



def write(name, category, hashtags, description, creatorUUID, createdTime, lastUpdateDateTime):
    db_instance = Db()
    session_table = db_instance.model.Session
    sql_session_table = _populate_session_model(session_table, name, category['value'], creatorUUID, createdTime, lastUpdateDateTime, description['value'], description['code'])
    session = db_instance.session
    try:
        session.add(sql_session_table)
        session.commit()

    except IntegrityError as ex:
        print(str(ex))
        session.rollback()
        return GeneralException(ex), 403

    except Exception as ex:
        print(str(ex))
        session.rollback()
        return GeneralException(ex), 403

    insertToSessionTag = writeToSessionTag(sql_session_table.UUID, hashtags, description['code'])

    if insertToSessionTag:
        return {'session_uuid' : sql_session_table.UUID}, 200
    
    else:
        return GeneralException(ex), 403
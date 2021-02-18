# Only in this file and its sibling / children)
# there should be reference/import to SQLAlchemy/Db().
# NO reference to flask.
# TODO-1: Finish the implementation of existing methods and add the new files / methods if needed

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import exc

from src.dal.db import Db
import uuid
from src.exc.app_exception import IntegrityException, ServerException, ConflictException, NotFoundException


def _populate_live_model(table_type, dt_from, dt_to, presenter_uuid, description, language, session_uuid):
    new_uuid = str(uuid.uuid4())
    table = table_type(UUID=new_uuid)
    table.StartAtGMT = dt_from
    table.EndsAtGMT = dt_to
    table.PresenterUUID = presenter_uuid
    table.SessionUUID = session_uuid
    table.Description = description
    table.LanguageISO = language
    return table


def _populate_liveTag_model(table_type, live_UUID, hashtags, languageISO):
    table = table_type(LiveUUID=live_UUID)
    table.Hashtag = ','.join(hashtags) if hashtags is not None else ''
    table.LanguageISO = languageISO
    return table


def writedt_to_live_tag(live_UUID, hashtags, languageISO):
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
        raise IntegrityException(str(ex))
    except Exception as ex:
        print(str(ex))
        liveTag.rollback()
        raise ServerException(str(ex))


def write(dt_from, dt_to, presenter_uuid, description, session_uuid, hashtags):
    db_instance = Db()
    session = db_instance.session
    live_table = db_instance.model.Live
    session_table = db_instance.model.Session
    try:
        language = session.query(session_table).filter(session_table.UUID == session_uuid).one()
    except exc.NoResultFound as ex:
        print(str(ex))
        session.rollback()
        raise NotFoundException('No such session found with UUID: ' + session_uuid)

    sql_live_table = _populate_live_model(live_table, dt_from, dt_to, presenter_uuid, description,
                                          language.LanguageISO, session_uuid)
    try:
        session.add(sql_live_table)
        if writedt_to_live_tag(sql_live_table.UUID, hashtags, language.LanguageISO):
            session.commit()
            return {'live_uuid': sql_live_table.UUID}
        else:
            raise ConflictException('There are conflicts, please contact support')

    except ConflictException as ex:
        print(str(ex))
        session.rollback()
        raise ConflictException(str(ex))
    except IntegrityError as ex:
        print(str(ex))
        session.rollback()
        raise IntegrityException('Request data not in proper format')
    except Exception as ex:
        print(str(ex))
        session.rollback()
        raise ServerException(str(ex))

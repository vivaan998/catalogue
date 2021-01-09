from sqlalchemy.orm import exc
from src.dal.db import Db


##
# ALL PACKs
##

def read_categories():
    db_instance = Db()
    session = db_instance.session
    t_categories = db_instance.model.Categories
    results = []
    try:
        results = session.query(t_categories).all()
    except exc.NoResultFound as ex:
        print(str(ex))
        pass

    return results


def read_category(category_languageISO):
    db_instance = Db()
    session = db_instance.session
    t_categories = db_instance.model.Categories

    result = None
    try:
        result = session.query(t_categories).filter(
            t_categories.LanguageISO == category_languageISO).all()
    except exc.NoResultFound as ex:
        print(str(ex))
        pass

    return result

from sqlalchemy.orm import exc
from src.dal.db import Db
from src.exc.app_exception import NotFoundException, ServerException


##
# ALL Categories based on language
##

def read_categories(category_languageISO):
    db_instance = Db()
    session = db_instance.session
    t_categories = db_instance.model.Categories

    try:
        result = session.query(t_categories).filter(t_categories.LanguageISO == category_languageISO).all()
        return result

    except exc.NoResultFound as ex:
        print(str(ex))
        raise NotFoundException('No categories found with ' + category_languageISO)
    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))

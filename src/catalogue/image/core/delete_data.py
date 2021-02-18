from sqlalchemy.orm import exc
from src.dal.db import Db
from src.exc.app_exception import NotFoundException, ServerException, FileNotFound
from config import basedir
import os


##
# Delete Image based on UUID
##

def delete(image_uuid):
    db_instance = Db()
    session = db_instance.session
    t_image = db_instance.model.Image
    try:
        query = session.query(t_image).filter(t_image.RefUUID == image_uuid).one()
        
        os.remove(query.Uri)  # Removing from local directory
        sessions = session.query(t_image).filter(t_image.RefUUID == image_uuid).delete()  # Removing from database
        if sessions:
            session.commit()
            return 'Successfully deleted'

    except NotFoundException as ex:
        print(str(ex))
        raise NotFoundException('Image UUID' + image_uuid + " not found")
    except FileNotFoundError as ex:
        sessions = session.query(t_image).filter(t_image.RefUUID == image_uuid).delete()
        if sessions:
            session.commit()
            raise FileNotFound('Image not found on server')

    except Exception as ex:
        print(str(ex))
        raise ServerException(str(ex))

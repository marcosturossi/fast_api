from sqlalchemy.orm import Session
from ..models import models
from ..models import data_base


class Manager:
    """ This method implement the normal user query in db"""

    @classmethod
    def create(cls, db: Session, **kwargs):
        """This class metho create a new insert in db.
        :param kwargs: Receive the method property for cls.
        :return: Return a instance of class that was created in db.
        """
        instance = cls(**kwargs)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance

    def get_by(self, id):
        return self.db.query(models.Book).filter(models.Book.id == id).first()

    def get_all(self):
        return self.db.query(models.Book).all()

from sqlalchemy.orm import Session


class Manager:
    """ This method implement the normal user query in db"""

    @classmethod
    def create(cls, db: Session, **kwargs):
        """
        This class method create a new insert in db.
        :param kwargs: Receive the method property for cls.
        :return: Return a instance of class that was created in db.
        """
        instance = cls(**kwargs)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance

    @classmethod
    def get_by(cls, db: Session, id: int):
        """
        Used to get get some object in db by id

        :param id: ID of object
        :return: An object
        """
        return db.query(cls).filter(cls.id == id).first()

    @classmethod
    def get_all(cls, db: Session):
        """
        This method return all instance of some table in db
        :param db: Session os Database connection
        :return List with all entities in database:
        """
        return db.query(cls).all()

    @classmethod
    def get_or_create(cls, db: Session, default: dict = None, **kwargs):
        """
        This method look at database, and if there are register
        return the register, if not create a new one.
        :param db: Session os Database connection.
        :param kwargs: This is the atribute of the class.
        :param default: This parameter is the atribute that search if use.
        :return: a object and a bool if created is returned True
        """
        instance = db.query(cls).filter_by(**default).first()
        create = False
        if not instance:
            instance = cls.create(db, **kwargs)
            create = True
        return instance, create

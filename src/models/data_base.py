from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DataBaseHandler:
    """ Decorator: que gerencia as conexoes do banco de dados
    """

    def __init__(self):
        self._connection_string = "postgresql://postgres:hd2biwnm@127.0.0.1:5432/fast"
        self.session = None

    def get_engine(self):
        """
        Inicializate a new engine for database connection
        :return: engine
        """
        engine = create_engine(self._connection_string, echo=True)
        return engine

    def __enter__(self):
        """
        Used to get in connection
        :return: the object
        """
        engine = self.get_engine()
        session = sessionmaker()
        self.session = session(autocommit=False, autoflush=False, bind=engine)
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the session when the operation finish
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: None
        """
        self.session.close()


# Dependecy
async def get_db():
    """
    This method is responsable for open and close the
    connections with database
    :return: db
    """
    with DataBaseHandler() as db:
        yield db


Base = declarative_base()

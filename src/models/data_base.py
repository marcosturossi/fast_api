from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DataBaseHandler:
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
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the session when the operation finish
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: None
        """
        self.session.close()


Base = declarative_base()


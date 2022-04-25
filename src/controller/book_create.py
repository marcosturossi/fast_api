from src.controller.base_crud import Manager
from src.models.books import Book
from sqlalchemy.orm import Session


class BookCreateController(Manager):
    """
    This Controller is resposable to create a new book:
    DO you need to pass a class in the class atribute
    """
    model = Book

    def __init__(self, db: Session, **kwargs):
        self.objects = self.create(db, **kwargs)

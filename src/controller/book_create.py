from src.controller.base_crud import Manager
from src.models.models import Book


class BookCreateController(Manager):
    """
    This Controller is resposable to create a new book:
    DO you need to pass a class in the class atribute
    """
    model = Book

    def __init__(self, db, **kwargs):
        self.object = self.create(db, **kwargs)

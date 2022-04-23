from src.controller.base_crud import Manager
from src.models.models import Book


class BookCreateController(Manager):
    model = Book

    def __init__(self, db, **kwargs):
        self.object = self.create(db, **kwargs)

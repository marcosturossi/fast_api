from src.controller.base_crud import Manager
from src.models.models import Book


class BookManager(Book, Manager):
    pass


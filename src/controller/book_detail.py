from .base_crud import Manager
from ..models.books import Book
from sqlalchemy.orm import Session


class BookDetailController(Manager):
    """
    This controller is responsable to get a book_by_id
    """
    model = Book

    def __init__(self, db: Session, book_id: int):
        self.object = self.get_by_id(db, book_id)

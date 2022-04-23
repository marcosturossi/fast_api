from src.controller.base_crud import Manager
from src.models.models import Book
from sqlalchemy.orm import Session


class BookDetailController(Manager):
    model = Book

    def __init__(self, db: Session, id: int):
        self.object = self.get_by_id(db, id)

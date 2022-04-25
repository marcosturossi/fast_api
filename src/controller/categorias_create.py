from src.models.categories import Category
from sqlalchemy.orm import Session
from .base_crud import Manager


class CategoryCreateController(Manager):
    """
    This controller is responsable to get a book_by_id
    """
    model = Category

    def __init__(self, db: Session, **kwargs):
        self.object = self.create(db, **kwargs)

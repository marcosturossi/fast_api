from src.models.categories import Categoria
from sqlalchemy.orm import Session
from .base_crud import Manager


class CategoriaCreate(Manager):
    """
    This controller is responsable to get a book_by_id
    """
    model = Categoria

    def __init__(self, db: Session, categoria_id: int):
        self.object = self.create(db, categoria_id)
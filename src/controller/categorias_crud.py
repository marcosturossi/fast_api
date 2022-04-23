from src.models import categories

from .base_crud import Manager


class CategoriasManager(Manager):
    models = categories.Categoria

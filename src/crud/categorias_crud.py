from src.models import models

from .base_crud import Manager


class CategoriasManager(Manager):
    models = models.Categoria

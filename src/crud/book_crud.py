from src.models import models
from . base_crud import Manager


class BookManager(Manager):
    models = models.Book


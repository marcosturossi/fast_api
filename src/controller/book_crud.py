from src.models import models
from . base_crud import Manager
from sqlalchemy.orm import Session
from ..models.models import Book


class BookManager(Book, Manager):
    pass


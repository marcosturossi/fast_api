from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.controller.book_create import BookManager
from src.schemas.book_schema import BookCreate, Book
from src.models.data_base import get_db

router = APIRouter()


@router.post("/book/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """
    This route insert a new book into a system
    :param book:
    :return a book:
    """
    book = BookManager(db, **book.dict())
    return book.object

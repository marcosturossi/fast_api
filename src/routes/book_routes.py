from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.controller.book_crud import BookManager
from src.schemas.book_schema import BookCreate, Book
from src.models.data_base import get_db

router = APIRouter()


@router.post("/book/", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Testando DOC STRING"""
    book = BookManager.create(db, **book.dict())
    return book

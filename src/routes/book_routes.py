from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.controller.book_create import BookCreateController
from src.controller.book_detail import BookDetailController
from src.schemas.book_schema import BookCreate, Book
from src.models.data_base import get_db

router = APIRouter()


@router.post("/book/", status_code=201, response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """
    This route insert a new book into a system
    :param book:
    :return a book:
    """
    book = BookCreateController(db, **book.dict())
    return book.object


@router.get('/book/{id}', response_model=Book)
def get_book(id: int, db: Session = Depends(get_db)):
    """
    This route can get the book by id
    :param id: id do livro
    :return Book
    """
    book = BookDetailController(db, id)
    return book.object

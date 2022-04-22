from fastapi import APIRouter
from src.crud.book_crud import BookManager
from src.schemas.book_schema import BookCreate, Book

router = APIRouter()


@router.post("/book/", response_model=BookCreate)
async def create_book(_book: BookCreate):
    book = BookManager()
    return book.create(_book.dict())

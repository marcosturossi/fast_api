from typing import List

from pydantic import BaseModel

from .book_schema import Book


class CategorySchemaBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CategorySchemaCreate(CategorySchemaBase):
    pass


class Category(CategorySchemaBase):
    id: int
    book: List[Book] = []

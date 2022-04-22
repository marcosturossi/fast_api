from typing import List

from pydantic import BaseModel

from .book_schema import Book


class CategoriaBase(BaseModel):
    nome: str

    class Config:
        orm_mode = True


class CategoriaCreate(CategoriaBase):
    pass


class Categoria(CategoriaBase):
    id: int
    book: List[Book] = []

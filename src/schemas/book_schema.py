from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    class Config:
        orm_mode = True


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    categoria_id: Optional[int]

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .data_base import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(63))

    book = relationship('Book', back_populates='category')

    def __repr__(self):
        return f"{self.nome}"

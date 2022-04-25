from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .data_base import Base


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(63))
    category_id = Column(Integer, ForeignKey('categories.id'))

    category = relationship("Category", back_populates='book')

    def __repr__(self):
        return f"{self.name}"

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .data_base import Base


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(63))
    categoria_id = Column(Integer, ForeignKey('categorias.id'))

    categoria = relationship("Categoria", back_populates='book')

    def __repr__(self):
        return f"{self.nome}"

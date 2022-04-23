from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .data_base import Base


class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(63))

    book = relationship('Book', back_populates='categoria')

    def __repr__(self):
        return f"{self.nome}"

    def nome_id(self):
        return f"{self.nome+str(self.id)}"


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(63))
    categoria_id = Column(Integer, ForeignKey('categorias.id'))

    categoria = relationship("Categoria", back_populates='book')

    def __repr__(self):
        return f"{self.nome}"
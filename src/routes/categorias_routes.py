from fastapi import APIRouter
from src.schemas.categorias_schema import CategoriaCreate, Categoria
from src.controller.categorias_crud import CategoriasManager

categoria_router = APIRouter()


@categoria_router.post('/categoria/', response_model=CategoriaCreate)
async def nova_categoria(_categoria: CategoriaCreate):
    categoria = CategoriasManager()
    return categoria.create(_categoria.dict())

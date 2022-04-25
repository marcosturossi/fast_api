from fastapi import APIRouter
from sqlalchemy.orm import Session
from src.schemas.categorias_schema import CategorySchemaCreate
from src.controller.categorias_create import CategoryCreateController

categoria_router = APIRouter()


@categoria_router.post('/category/', response_model=CategorySchemaCreate)
async def new_category(db: Session, _category: CategorySchemaCreate):
    category = CategoryCreateController(db, **_category.dict())
    return category.object

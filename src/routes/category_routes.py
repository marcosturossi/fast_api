from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.categories_schema import CategorySchemaCreate
from src.controller.categories_create import CategoryCreateController
from src.models.data_base import get_db

category_router = APIRouter()


@category_router.post('/category/', response_model=CategorySchemaCreate)
def new_category(category: CategorySchemaCreate, db: Session = Depends(get_db)):
    categoria = CategoryCreateController(db, **category.dict())
    return categoria.object

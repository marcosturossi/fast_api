from fastapi import FastAPI
from src.routes.book_routes import router
from src.routes.category_routes import category_router
from src.models.data_base import DataBaseHandler, Base
from src.controller import book_create, categories_create


app = FastAPI()
# Inclui uma rota no app
app.include_router(router)
app.include_router(category_router)


Base.metadata.create_all(bind=DataBaseHandler().get_engine())








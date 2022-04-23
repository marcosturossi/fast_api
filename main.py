from fastapi import FastAPI
from src.routes.book_routes import router
from src.routes.categorias_routes import categoria_router
from src.models.data_base import DataBaseHandler, Base
from src.controller import book_create, categorias_crud


app = FastAPI()
# Inclui uma rota no app
app.include_router(router)
app.include_router(categoria_router)


Base.metadata.create_all(bind=DataBaseHandler().get_engine())








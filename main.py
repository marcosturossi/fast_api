from fastapi import FastAPI
from src.routes.book_routes import router
from src.routes.categorias_routes import categoria_router
from src.models import data_base, models
from src.crud import book_crud, categorias_crud


app = FastAPI()
# Inclui uma rota no app
app.include_router(router)
app.include_router(categoria_router)

data_base.Base.metadata.create_all(bind=data_base.engine)

book = book_crud.BookManager()
categorias_crud.CategoriasManager()








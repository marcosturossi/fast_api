import json

from fastapi.testclient import TestClient
from main import app
from src.controller.book_crud import BookManager

client = TestClient(app)


def test():
    response = client.post('http://127.0.0.1:8000/book/', data=json.dumps({'nome': 'Game of Thrones'}))
    print(json.loads(response.text))

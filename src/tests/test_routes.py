import json

from fastapi.testclient import TestClient
from main import app
from src.controller.book_create import BookCreateController

client = TestClient(app)


def test():
    response = client.post('http://127.0.0.1:8000/book/', data=json.dumps({'nome': 'Game of Thrones'}))
    assert response.status_code == 200
    print(json.loads(response.text))


def test_id():
    response = client.get('http://127.0.0.1:8000/book/21/')
    print(json.loads(response.text))
    assert response.status_code == 200


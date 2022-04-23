import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test():
    """This teste verirfy if the book create end-point is working"""
    response = client.post('http://127.0.0.1:8000/book/', data=json.dumps({'nome': 'Game of Thrones'}))
    print(json.loads(response.text))


def test_id():
    """This teste verify if the get book by id is working"""
    response = client.get('http://127.0.0.1:8000/book/1/')
    assert response.status_code == 200

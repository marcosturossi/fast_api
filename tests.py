import requests
import json as js


def test():
    response = requests.post('http://127.0.0.1:8000/book', data=js.dumps(
        {'nome': 'Nescau'}))
    print(response.text)
    response1 = requests.post('http://127.0.0.1:8000/categoria', data=js.dumps(
        {'nome': 'Nescau'}))
    print(response1.text)


if __name__=='__main__':
    test()
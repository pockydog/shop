import requests


class Test:
    _URL = 'http://127.0.0.1:5000/product/pic'

    @classmethod
    def add_info(cls):
        files = {'files': open('/Users/vicky/Desktop/123.jpeg', 'rb')}
        payload = {
            'product_id': 2,
            'description': 'testtttttttttttttttttttt',
            'remark': 'testtttttttttttttttttttt',
        }
        response = requests.post(url=cls._URL, files=files, json=payload)
        print(response.text)
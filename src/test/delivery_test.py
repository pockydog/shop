import requests


class Test:
    URL = 'http://127.0.0.1:5000/delivery'
    @classmethod
    def add_info(cls):
        payload = {
            'name': '',
            'price': 100,
            'description': '123',
            'is_active': 0,
            'remark': '1234567ygfdr56ygfre',
        }
        response = requests.post(url=cls.URL, json=payload)
        print(response.text)
import requests


class Test:
    _URL = 'http://127.0.0.1:8022/product/pic'

    @classmethod
    def add_info(cls):
        files = [
            ('image', open('/Users/vicky/Desktop/123.jpeg', 'rb')),
            ('image', open('/Users/vicky/Desktop/123.jpeg', 'rb'))]
        payload = {
            'product_id': 2,
            'description': 'testtttttttttttttttttttt',
            'remark': 'testtttttttttttttttttttt',
        }
        response = requests.post(url=cls._URL, files=files, data=payload)
        print(response.text)


if __name__ == '__main__':
    Test.add_info()

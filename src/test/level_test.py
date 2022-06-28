import requests


class Test:
    url = 'http://127.0.0.1:5000/level'
    @classmethod
    def add_info(cls):
        url = cls.url
        member = ['Newbie', 'Registered', 'Advanced', 'Respectful', 'VIP']
        for i in member:
            response = requests.post(url=url, params={'name': f'{i}'})
            print(response.text)

    @classmethod
    def del_info(cls):
        url = 'http://127.0.0.1:5000/level'
        response = requests.delete(url=url, params={'level_id': 3})
        print(response.text)

    @classmethod
    def get_info(cls):
        url = 'http://127.0.0.1:5000/level'
        response = requests.get(url=url)
        print(response.text)

    @classmethod
    def update_info(cls):
        url = 'http://127.0.0.1:5000/level'
        response = requests.update(url=url)
        print(response.text)
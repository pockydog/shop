import requests
from faker import Faker
fake = Faker()


class Test:
    _URL = 'http://127.0.0.1:5000/user'

    @classmethod
    def get_info(cls):
        response = requests.get(url=cls._URL)
        print(response.text)

    @classmethod
    def add_info(cls):
        for i in range(10):
            payload = {
                'name': f'{fake.first_name()}',
                'username': f'{fake.unix_time()}',
                'password': f'{fake.unix_time()}',
                'phone_number': f'{fake.phone_number()}',
            }
            response = requests.post(url=cls._URL, json=payload)
            print(response.text)

    @classmethod
    def del_info(cls):
        response = requests.delete(url=cls._URL, params={'name': 'Holly', 'phone_number': '5770817122'})
        print(response.text)

    @classmethod
    def update_info(cls):
        payload = {
            'password': f'New{fake.unix_time()}',
            'phone_number': f'New{fake.phone_number()}',
        }
        response = requests.put(url=cls._URL, json=payload, params={'account': '993392921'})
        print(response.text)

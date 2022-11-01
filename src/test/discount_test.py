import requests


class Test:
    url = 'http://127.0.0.1:5000/discount'

    @classmethod
    def add_info(cls):
        payload = {
            'name': 'discount',
            'price': 20,
            'level_id': 1,
            'open_date': '2021-03-02',
            'end_date': '2021-03-04',
            'is_active': 0,
            'remark': '34242',
        }
        response = requests.post(url=cls.url, json=payload)
        print(response.text)

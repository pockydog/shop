import requests

class Test:
    url = 'http://127.0.0.1:5000/product'
    _INFO = ['spring onion', 'onion', 'garlic', 'garlic sprout', 'ginger']

    @classmethod
    def add_info(cls):
        for i in range(len(cls._INFO)):
            response = requests.post(
                url=cls.url,
                json={
                    'name': cls._INFO[i],
                    'description': f'description_{cls._INFO[i]}',
                    'product_type_id': 1,
                    'discount_id': None,
                    'stock': 0,
                    'sale_price': 10,
                    'cost_price': 10,
                    'remark': '10000000',
                }
            )
            print(response.text)

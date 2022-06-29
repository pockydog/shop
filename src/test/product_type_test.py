import requests


class Test:
    url = 'http://127.0.0.1:5000/product/type'
    _Type = ['instant_noodles', 'vegetables', 'fruit', 'oil', 'salad']
    _smile = ['noodles', 'veg', 'fru', 'oil', 'sal']
    _code = ['101', '102', '103', '104', '105']

    @classmethod
    def add_info(cls):
        for i in range(len(cls._Type)):
            response = requests.post(
                url=cls.url,
                json={
                    'name': cls._Type[i],
                    'short_name': cls._smile[i],
                    'code': cls._code[i],
                    'remark': '1'
                }
            )
            print(response.text)

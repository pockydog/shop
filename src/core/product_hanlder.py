from modles.product_models import ProductType
from app import db

class ProductTypeHanlders:

    @classmethod
    def get_info(cls):
        conditions = list()
        results = list()
        products = db.session.query(ProductType).filter(*conditions).all()
        for product in products:
            result = {
                'id': product.id,
                'name': product.name,
                'type': product.type,
                'code': product.code,
            }
            results.append(result)
        return result

    @classmethod
    def add_info(cls, name, type_, code):
        product = ProductType(
            name=name,
            type=type_,
            code=code,
        )
        db.session.add(product)
        db.session.commit()
        return {'ok': 'ok'}
from models.product_models import ProductType
from app import db


class ProductTypeHanlder:
    @classmethod
    def get_info(cls, short_name):
        conditions = list()
        results = list()
        if short_name:
            conditions.append(ProductType.short_name == short_name)
        products = db.session.query(ProductType).filter(*conditions).all()
        for product in products:
            result = {
                'id': product.id,
                'name': product.name,
                'short_name': product.short_name,
                'code': product.code,
                'remark': product.remark
            }
            results.append(result)
        return results

    @classmethod
    def add_info(cls, name, short_name, code, remark):
        if not isinstance(name, str) and not isinstance(short_name, str) and not isinstance(code, int) and not isinstance(remark, str):
            raise ValueError('Wrong format . ')
        product = ProductType(
            name=name,
            short_name=short_name,
            code=code,
            remark=remark,
        )
        db.session.add(product)
        result = {
            'name': product.name,
            'short_name': product.short_name,
            'code': product.code,
            'remark': product.remark,
        }
        db.session.commit()
        return result

    @classmethod
    def del_info(cls, short_name):
        if not isinstance(short_name, str):
            raise ValueError('Short Name Not Exist . ')
        product = db.session.query(ProductType).filter(ProductType.short_name == short_name).first()
        if not product:
            raise ValueError('Info Not Found . ')
        db.session.delete(product)
        db.session.commit()

    @classmethod
    def update_info(cls, short_name):
        product = db.session.query(ProductType).filter(ProductType.short_name == short_name).first()
        db.session.add(product)
        db.session.commit()

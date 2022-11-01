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
        if not isinstance(name, str) and not isinstance(short_name, str) and not isinstance(code, int):
            raise ValueError('Wrong format . ')
        if not isinstance(remark, str) and remark is not None:
            raise ValueError('Remark Wrong Format')
        product = ProductType(
            name=name,
            short_name=short_name,
            code=code,
            remark=remark,
        )
        db.session.add(product)
        db.session.flush()

        result = {
            'name': product.name,
            'short_name': product.short_name,
            'code': product.code,
            'remark': product.remark,
            'create_datetime': product.create_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'update_datetime': product.update_datetime.strftime("%Y-%m-%d %H:%M:%S"),
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

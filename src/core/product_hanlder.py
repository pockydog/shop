from models.product_models import Product, ProductType, Discount
from app import db


class ProductHanlder:
    @classmethod
    def get_info(cls):
        conditions = list()
        results = list()
        products = db.session.query(Product).filter(*conditions).all()
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
    def add_info(cls, name, description, discount_id, product_type_id, stock, sale_price, cost_price, remark):
        if not isinstance(name, str) and not isinstance(product_type_id, int) and not isinstance(stock, int) and not \
                isinstance(sale_price, int) and not isinstance(cost_price, int):
            raise ValueError('Info Wrong format')
        product_type = db.session.query(ProductType).filter(ProductType.id == product_type_id).first()
        if not product_type:
            raise ValueError('product type not found')
        if discount_id is not None:
            discount = db.session.query(Discount).filter(Discount.id == discount_id).first()
            if not discount:
                raise ValueError('discount not found')
        if sale_price <= 0 or cost_price <= 0:
            raise ValueError('amount cannot be negative')
        if stock < 0:
            raise ValueError('Stock amount cannot be negative')
        product = Product(
            name=name,
            description=description,
            discount_id=discount_id,
            product_type_id=product_type_id,
            stock=stock,
            sale_price=sale_price,
            cost_price=cost_price,
            remark=remark,
        )
        db.session.add(product)
        db.session.flush()
        result = {
            'id': product.id,
            'name': name,
            'description': description,
            'discount_id': discount_id,
            'product_type_id': product_type_id,
            'stock': stock,
            'sale_price': sale_price,
            'cost_price': cost_price,
            'remark': remark,
        }
        db.session.commit()
        return result


    # @classmethod
    # def del_info(cls):
    #     product = db.session.query(ProductType).filter
from app import db
from models.product_models import Order, User, Product, Delivery, Discount
from const import OrderStatus


class OrderHandler:
    @classmethod
    def add_info(cls, product_price, delivery_price, product_id, user_id, discount_id, delivery_id, city, township,
                 road, remark):
        if not isinstance(product_price, str) and not isinstance(delivery_price, int) \
                and not isinstance(city, str) and not isinstance(township, str) \
                and not isinstance(road, str) and not isinstance(product_id, int) \
                and not isinstance(delivery_id, int) and not isinstance(user_id, int):
            raise ValueError('Wrong Format')
        product_price = db.session(Product).filter(Product.id == product_id).first()
        if product_price < 0:
            product_price = product_price.sale_price * product_price
        # if product_price < 0 and delivery_price < 0:
        #     raise ValueError('Amount Cannot Be Negative')
        if not isinstance(remark, int) or remark is not None:
            raise ValueError('Remark Wrong Format')
        if not isinstance(discount_id, int) or discount_id is not None:
            raise ValueError('Discount Id Wrong Format')
        product = db.session.query(Product).filter(Product.product_id == product_id).first()
        if not product:
            raise ValueError('Product Id Not Found')
        user = db.session.query(User).filter(User.user_id == user_id).first()
        if not user:
            raise ValueError('User Id Not Found')
        delivery = db.session.query(Delivery).filter(Delivery.delivery_id == delivery_id).first()
        if not delivery:
            raise ValueError('Delivery Id Not Found')
        if discount_id:
            discount = db.session.query(Discount).filter(Discount.discount_id == discount_id).first()
            if not discount:
                raise ValueError('Discount Id Not Found')
        order = Order(
            product_price=product_price,
            delivery_price=delivery_price,
            product_id=product_id,
            user_id=user_id,
            discount_id=discount_id,
            delivery_id=delivery_id,
            city=city,
            township=township,
            road=road,
            remark=remark,
            status=OrderStatus.PENDING
        )
        db.session.add(order)
        db.session.flush()
        result = {
            'id': order.id,
            'product_price': order.product_price,
            'delivery_price': order.delivery_price,
            'product_id': order.product_id,
            'user_id': order.user_id,
            'discount_id': order.discount_id,
            'delivery_id': order.delivery_id,
            'city': order.city,
            'township': order.township,
            'road': order.road,
            'remark': order.remark,
            'status': order.status,
            'create_datetime': order.create_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'update_datetime': order.update_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        }
        db.session.commit()
        return result

    @classmethod
    def test_info(cls):
        product_price = db.session.query(Product).filter(Product.id == 2).first()
        print(product_price.sale_price)

    # @classmethod
    # def get_info(cls, username):
    #     orders = db.session.query(
    #         Order.id,
    #         Order.price,
    #         User.name.label('username'),
    #         User.phone_number,
    #         Product.name.label('product_name')
    #     ).join(
    #         User, User.id == Order.user_id
    #     ).join(
    #         Product, Product.id == Order.product_id
    #     ).all()
    #     for order in orders:
    #         print(order)

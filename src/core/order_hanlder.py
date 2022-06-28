from app import db
from modles.product_models import Order, User, Product



class OrderHandler:
    @classmethod
    def get_info(cls, username):
        orders = db.session.query(
            Order.id,
            Order.price,
            User.name.label('username'),
            User.phone_number,
            Product.name.label('product_name')
        ).join(
            User, User.id == Order.user_id
        ).join(
            Product, Product.id == Order.product_id
        ).all()
        for order in orders:
            print(order)
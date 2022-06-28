from test.user_test import *


if __name__ == "__main__":
    Test.add_info()
from app import db


# class OrderHandler:
#     @classmethod
#     def get_info(cls):
#         orders = db.session.query(
#             Order.id,
#             Order.price,
#             User.name.label('username'),
#             User.phone_number,
#             Product.name.label('product_name')
#         ).join(
#             User, User.id == Order.user_id
#         ).join(
#             Product, Product.id == Order.product_id
#         ).all()
#         for order in orders:
#             print(order)
#


import pytz

from app import db
from sqlalchemy import func, distinct, cast
from models.product_models import Product, Discount, Level

result = db.session.query(
            func.count(distinct(Product.name))   # 根據此欄位 若此欄位名字並用(distinct)方法為相同則不另多計算
        ).filter(
            Product.cost_price == 200,
        ).scalar()

print(result)

results = db.session.query(
            Discount.price,
            Discount.id,
            Level.create_datetime.label('level'),
        ).join(
            Level, Level.id == Discount.level_id
        ).all()
# print(results[:10])
# print(len(results) if results else 0)

result = db.session.query(
            cast(func.sum(Discount.price), db.Integer)
        ).scalar()


_IST_TIMEZONE_NAME = 'Asia/Kolkata'
TW = 'Asia/Taipei'
IST_TIMEZONE = pytz.timezone(_IST_TIMEZONE_NAME)
TW = pytz.timezone(TW)

from datetime import datetime
print('-----------------------------')
print(datetime.now())
print(datetime.now(tz=IST_TIMEZONE))
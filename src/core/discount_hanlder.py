from datetime import datetime

from models.product_models import Discount, Level
from app import db


class DiscountHanlder:
    @classmethod
    def add_info(cls, name, price, level_id, open_date, end_date, is_active, remark):
        if not isinstance(name, str) and not isinstance(price, int):
            raise ValueError('Info Wrong format')
        if price <= 0:
            raise ValueError('Amount cannot be negative')
        if not isinstance(remark, str) and remark is not None:
            raise ValueError('Remark Wrong format')
        if not isinstance(level_id, int) and level_id is not None:
            raise ValueError('Level id Wrong format')
        if level_id is not None:
            level = Level.query.filter(Level.id == level_id).first()
            if not level:
                raise ValueError('level id not found')
        open_date = datetime.strptime(open_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        if end_date < open_date:
            raise ValueError('結束日期不能大於起始期')
        discount = Discount(
            name=name,
            price=price,
            level_id=level_id,
            open_date=open_date,
            end_date=end_date,
            is_active=is_active,
            remark=remark,
        )

        db.session.add(discount)
        db.session.flush()
        result = {
            'id': discount.id,
            'name': discount.name,
            'price': discount.price,
            'level_id': discount.level_id,
            'open_date': discount.open_date.strftime("%Y-%m-%d"),
            'end_date': discount.end_date.strftime("%Y-%m-%d"),
            'is_active': discount.is_active,
            'remark': discount.remark,
            'create_datetime': discount.create_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'update_datetime': discount.update_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        }
        db.session.commit()
        return result

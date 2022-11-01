from models.product_models import Delivery
from app import db


class DeliverHanlder:
    @classmethod
    def add_info(cls, name, price, description, remark):
        if not isinstance(name, str) and not isinstance(price, int):
            raise ValueError('Wrong Format')
        if not name:
            raise ValueError('Name cannot be empty')
        if not isinstance(description, str) and description is not None:
            raise ValueError('Description Wrong format')
        if price < 0:
            raise ValueError('Amount cannot be negative')

        delivery = Delivery(
            name=name,
            price=price,
            description=description,
            remark=remark
        )
        db.session.add(delivery)
        db.session.flush()
        result = {
            'id': delivery.id,
            'name': delivery.name,
            'price': delivery.price,
            'description': delivery.description,
            'is_active': delivery.is_active,
            'remark': delivery.remark,
            'create_datetime': delivery.create_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'update_datetime': delivery.update_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        }
        db.session.commit()
        return result

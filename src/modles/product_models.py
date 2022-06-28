from sqlalchemy import func
from app import db


class Level(db.Model):
    __tablename__ = 'level'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_active = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')
    name = db.Column(db.String(90), nullable=True)
    remark = db.Column(db.String(100))
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(90), nullable=True)
    account = db.Column(db.Integer, nullable=True)
    password = db.Column(db.String(90), nullable=True)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'))
    phone_number = db.Column(db.String(90), nullable=False)
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    order = db.relationship('Order', backref='user')


class ProductType(db.Model):
    __tablename__ = 'product_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(900), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    code = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000))
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())



class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    product_type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'))
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())



class ProductPic(db.Model):
    __tablename__ = 'product_pic'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pic_url = db.Column(db.String(1000))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    description = db.Column(db.String(1000))
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class DeliveryFee(db.Model):
    __tablename__ = 'delivery_fee'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(900), nullable=False)
    price = db.Column(db.Integer)
    description = db.Column(db.String(500))
    is_active = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class Discount(db.Model):
    __tablename__ = 'discount'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Integer)
    price = db.Column(db.Integer)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'))
    is_active = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    discount_id = db.Column(db.Integer, db.ForeignKey('discount.id'))
    delivery_fee_id = db.Column(db.Integer, db.ForeignKey('delivery_fee.id'))

    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


# db.create_all()
# db.session.commit()

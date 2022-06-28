from sqlalchemy import func
from app import db


class Level(db.Model):
    __tablename__ = 'level'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_active = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')
    name = db.Column(db.String(90), nullable=False)
    remark = db.Column(db.String(100))
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(90))
    account = db.Column(db.String, nullable=False)
    password = db.Column(db.String(90), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), server_default='1')
    phone_number = db.Column(db.String(90), nullable=False)
    remark = db.Column(db.String(100))
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class ProductType(db.Model):
    __tablename__ = 'product_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(900), nullable=False)
    short_name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000))
    is_open = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')
    stock = db.Column(db.Integer)
    is_delete = db.Column(db.Boolean, comment='是否開啟：0:否 1:是')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    discount_id = db.Column(db.Integer, db.ForeignKey('discount.id'))
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


class Delivery(db.Model):
    __tablename__ = 'delivery'
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
    open_date = db.Column(db.DateTime, server_default=None)
    end_date = db.Column(db.DateTime, server_default=None)
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
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.id'))
    city = db.Column(db.String(50), nullable=False, comment='縣市')
    township = db.Column(db.String(50), nullable=False, comment='鄉鎮區')
    road = db.Column(db.String(50), nullable=False, comment='地址')
    remark = db.Column(db.String(100), nullable=False, comment='備註')
    status = db.Column(db.Integer, nullable=False, server_default='1',
                       comment='1: 已下訂, 2: 付款失敗, 3: 逾期 未付款, 4: 付款成功, 5: 已出貨, 6: 已送達, 7: 退貨, 8: 退款完成')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


# db.create_all()
# db.session.commit()

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
    account = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), server_default='1')
    phone_number = db.Column(db.String(50), nullable=False)
    is_block = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')
    remark = db.Column(db.String(100))
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class ProductType(db.Model):
    __tablename__ = 'product_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    short_name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000))
    remark = db.Column(db.String(100), comment='備註')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000))
    discount_id = db.Column(db.Integer, db.ForeignKey('discount.id'))
    product_type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'))
    stock = db.Column(db.Integer, nullable=False)  # 庫存
    sale_price = db.Column(db.Integer, nullable=False)
    cost_price = db.Column(db.Integer, nullable=False)
    is_open = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')  # 是否開
    is_delete = db.Column(db.Boolean, comment='是否開啟：0:否 1:是')  # 是否下架
    remark = db.Column(db.String(100), nullable=False, comment='備註')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class ProductPic(db.Model):
    __tablename__ = 'product_pic'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pic_url = db.Column(db.String(1000))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    description = db.Column(db.String(1000))
    remark = db.Column(db.String(100), nullable=False, comment='備註')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class Delivery(db.Model):
    __tablename__ = 'delivery'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer)
    description = db.Column(db.String(500))
    is_active = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')
    remark = db.Column(db.String(100), nullable=False, comment='備註')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class Discount(db.Model):
    __tablename__ = 'discount'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'))
    open_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    is_active = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')
    remark = db.Column(db.String(100), nullable=False, comment='備註')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_price = db.Column(db.Integer, nullable=False)
    delivery_price = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    discount_id = db.Column(db.Integer, db.ForeignKey('discount.id'))
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.id'))
    city = db.Column(db.String(50), nullable=False, comment='縣市')
    township = db.Column(db.String(50), nullable=False, comment='鄉鎮區')
    road = db.Column(db.String(50), nullable=False, comment='地址')
    remark = db.Column(db.String(100), nullable=False, comment='備註')
    status = db.Column(db.Integer, nullable=False, server_default='0',
                       comment='0:處理中 1: 成功, 2:失敗, 3：已寄出')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


# db.create_all()
# db.session.commit()

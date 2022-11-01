from sqlalchemy import func
from app import db


class Level(db.Model):
    __tablename__ = 'level'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_active = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')
    name = db.Column(db.String(90), nullable=False, comment='等級名稱')
    remark = db.Column(db.String(300), comment='備註')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), comment='用戶名稱')
    role = db.Column(db.Integer, comment='角色：1:管理員 2:會員')
    username = db.Column(db.String(100), nullable=False, comment='用戶帳號')
    password = db.Column(db.String(100), nullable=False, comment='用戶密碼')
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), server_default='1', comment='等級id')
    phone_number = db.Column(db.String(100), nullable=False, comment='電話號碼')
    is_block = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')
    remark = db.Column(db.String(300), comment='備註')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class ProductType(db.Model):
    __tablename__ = 'product_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, comment='商品分類')
    short_name = db.Column(db.String(100), nullable=False, comment='商品分類縮寫')
    code = db.Column(db.Integer, nullable=False, comment='商品分類代碼')
    remark = db.Column(db.String(300), comment='備註')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, comment='商品名稱')
    description = db.Column(db.Text, comment='商品描述')
    discount_id = db.Column(db.Integer, db.ForeignKey('discount.id'), comment='折扣id')
    product_type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'), nullable=False, comment='商品分類id')
    stock = db.Column(db.Integer, nullable=False, comment='庫存')
    sale_price = db.Column(db.Integer, nullable=False, comment='定價')
    cost_price = db.Column(db.Integer, nullable=False, comment='成本價')
    is_open = db.Column(db.Boolean, server_default='0', comment='是否下架：0:否 1:是')
    is_delete = db.Column(db.Boolean, comment='是否刪除：0:否 1:是')
    remark = db.Column(db.String(300), comment='備註')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class ProductPic(db.Model):
    __tablename__ = 'product_pic'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), comment='商品id')
    description = db.Column(db.String(1000), comment='商品圖片描述')
    remark = db.Column(db.String(100), nullable=False, comment='備註')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class Delivery(db.Model):
    __tablename__ = 'delivery'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, comment='運費方式名稱')
    price = db.Column(db.Integer, comment='運費')
    description = db.Column(db.String(500), comment='運費描述')
    is_active = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')
    remark = db.Column(db.String(300), nullable=False, comment='備註')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class Discount(db.Model):
    __tablename__ = 'discount'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), comment='折扣名稱')
    price = db.Column(db.Integer, comment='折扣金額')
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), comment='會員等級id')
    open_date = db.Column(db.Date, comment='開始日期')
    end_date = db.Column(db.Date, comment='結束日期')
    is_active = db.Column(db.Boolean, server_default='0', comment='是否開啟：0:否 1:是')
    remark = db.Column(db.String(300), nullable=False, comment='備註')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_price = db.Column(db.Integer, nullable=False, comment='商品金額')
    delivery_price = db.Column(db.Integer, nullable=False, comment='運費金額')
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False, comment='商品id')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment='會員id')
    discount_id = db.Column(db.Integer, db.ForeignKey('discount.id'),  comment='折扣id')
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.id'), nullable=False, comment='費用id')
    city = db.Column(db.String(50), nullable=False, comment='縣市')
    township = db.Column(db.String(50), nullable=False, comment='鄉鎮區')
    road = db.Column(db.String(50), nullable=False, comment='地址')
    remark = db.Column(db.String(300), comment='備註')
    status = db.Column(db.Integer, nullable=False,
                       comment='1:待處理 2: 處理中, 3:已寄出, 4：成功, 5:失敗')
    create_datetime = db.Column(db.DateTime, server_default=func.now())
    update_datetime = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


# db.create_all()
# db.session.commit()

from models.product_models import User
from app import db


class UserHanlder:
    @classmethod
    def get_info(cls, phone_number):
        conditions = list()
        results = list()
        if phone_number:
            conditions.append(User.phone_number == phone_number)
        users = db.session.query(User).filter(*conditions).all()
        for user in users:
            result = {
                'id': user.id,
                'name': user.name,
                'username': user.username,
                'password': user.password,
                'level_id': user.level_id,
                'phone_number': user.phone_number,
                'create_datetime': user.create_datetime.strftime("%Y-%m-%d %H:%M"),
                'update_datetime': user.update_datetime.strftime("%Y-%m-%d %H:%M"),
            }
            results.append(result)
        return results

    @classmethod
    def add_info(cls, name, username, password, phone_number):
        if not isinstance(name, str) and isinstance(username, str) and isinstance(password, int) and isinstance(phone_number, str):
            raise ValueError('wrong format .')
        user = User(
            name=name,
            username=username,
            password=password,
            phone_number=phone_number,
        )
        if not user:
            raise ValueError('info error ')

        db.session.add(user)
        db.session.commit()
        results = {
            'id': user.id,
            'name': user.name,
            'username': user.username,
            'password': user.password,
            'phone_number': user.phone_number,
            'level_id': user.level_id,
        }
        return results, {'success': True}

    @classmethod
    def del_info(cls, name, phone_number):
        conditions = list()
        if name:
            conditions.append(User.name == name)
        if phone_number:
            conditions.append(User.phone_number == phone_number)
        user = db.session.query(User).filter(*conditions).first()
        if not user:
            raise ValueError('Name Or Phone Number Incorrect')
        db.session.delete(user)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, username, phone_number, password):
        if not isinstance(username, str):
            raise ValueError('Account wrong format . ')
        user = db.session.query(User).filter(User.username == username).first()
        if not user:
            raise ValueError('Username not exist . ')
        if not isinstance(phone_number, str):
            raise ValueError('Phone Number wrong format . ')
        if not isinstance(password, str):
            raise ValueError('Password wrong format . ')
        user.phone_number = phone_number
        user.password = password
        db.session.add(user)
        result = {
            'id': user.id,
            'name': user.name,
            'username': user.username,
            'password': user.password,
            'phone_number': user.phone_number,
            'level_id': user.level_id,
        }
        db.session.commit()
        return result, {'success': True}


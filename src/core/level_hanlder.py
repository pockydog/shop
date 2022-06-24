from modles.product_models import Level
from app import db


class LevelHanlder:
    @classmethod
    def add_info(cls):
        level = Level(
            name='VIP',
        )
        db.session.add(level)
        db.session.commit()
        return {'success': True}

    @classmethod
    def get_info(cls):
        conditions = list()
        result_list = list()
        levels = db.session.query(Level).filter(*conditions).all()
        for level in levels:
            result = {
                'id': level.id,
                'name': level.name,
                'is_active': level.is_active,
                'create_datetime': level.create_datetime,
                'update_datetime': level.update_datetime,

            }
            result_list.append(result)
        return result_list

    @classmethod
    def del_info(cls):
        pass

    @classmethod
    def update_info(cls):
        pass
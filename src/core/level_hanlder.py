from modles.product_models import Level
from app import db


class LevelHanlder:
    @classmethod
    def add_info(cls, name):
        if not isinstance(name, str):
            raise ValueError('wrong format')
        level = Level(
            name=name,
        )
        db.session.add(level)
        db.session.commit()
        return {'success': True}

    @classmethod
    def get_info(cls, name):
        conditions = list()
        results = list()
        if name:
            conditions.append(Level.name == name)
        levels = db.session.query(Level).filter(*conditions).all()
        for level in levels:
            result = {
                'id': level.id,
                'name': level.name,
                'is_active': level.is_active,
                'create_datetime': level.create_datetime.strftime("%Y-%m-%d %H:%M"),
                'update_datetime': level.update_datetime.strftime("%Y-%m-%d %H:%M"),
            }
            results.append(result)
        return results

    @classmethod
    def del_info(cls, level_id):
        if not isinstance(level_id, int):
            raise ValueError('wrong format')
        levels = db.session.query(Level).filter(Level.id == level_id).first()
        if not levels:
            raise ValueError('level id not found')
        db.session.delete(levels)
        db.session.commit()
        return {'success': True}

    @classmethod
    def update_info(cls, level_id):
        if not level_id:
            raise ValueError('Wrong format.')
        level = db.session.query(Level).filter(Level.id == level_id).first()
        result = {
            'id': level.id,
            'name': level.name,
            'is_active': level.is_active,
            'create_datetime': level.create_datetime.strftime("%Y-%m-%d %H:%M"),
            'update_datetime': level.update_datetime.strftime("%Y-%m-%d %H:%M"),
        }
        db.session.commit()
        return result



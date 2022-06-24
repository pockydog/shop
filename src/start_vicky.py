from modles.product_models import Level
from app import db


class LevelHanlder:
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
        print(result_list)
        return result_list
            # paginate(
            # page=page,
            # per_page=per_page,
            # error_out=False
        # )
        # pager = {
        #     'page': level.page,
        #     'per_page': level.per_page,
        #     'totle_page': level.pages
        # }


if __name__ == ' __main__':
    print(LevelHanlder.get_info())



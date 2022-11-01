from models.product_models import ProductPic
from app import db
from config import Config


class ProductPicHanlder:
    @classmethod
    def get_info(cls):
        pass

    @classmethod
    def add_info(cls,  product_id, description, remark, images):
        if not isinstance(product_id, int) and not isinstance(description, str):
            raise ValueError('Wrong Format')
        if not isinstance(remark, str) and remark is not None:
            raise ValueError('Remark Wrong Format')
        for image in images:
            product_pic = ProductPic(
                product_id=product_id,
                description=description,
                remark=remark,
            )
            db.session.add(product_pic)
            db.session.flush()
            image.save(f'{Config.IMAGE_PATH}/{product_pic.id}.jpg')
        db.session.commit()
        return {'success': 'True'}

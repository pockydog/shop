from models.product_models import *
from app import db

if __name__ == "__main__":
    db.create_all()
    db.session.commit()

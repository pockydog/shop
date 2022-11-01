from flask import request, jsonify
from core.product_pic_hanlder import ProductPicHanlder
from app import app
import os


@app.route('/product/pic', methods=['POST'])
def add_product_pic_hanlder():
    images = request.files.getlist('image')
    print(images)
    payload = request.form
    product_id = payload['product_id']
    description = payload['description']
    remark = payload['remark']
    result = ProductPicHanlder.add_info(product_id=product_id, description=description, remark=remark, images=images)
    return jsonify(result=result)

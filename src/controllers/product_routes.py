from flask import request, jsonify

from core.product_hanlder import ProductHanlder
from app import app


# @app.route('/product', methods=['GET'])
# def get_product_info():
#     product = ProductHanlder()

@app.route('/product', methods=['POST'])
def add_product_info():
    payload = request.get_json()
    name = payload['name']
    description = payload['description']
    discount_id = payload['discount_id']
    product_type_id = payload['product_type_id']
    stock = payload['stock']
    sale_price = payload['sale_price']
    cost_price = payload['cost_price']
    remark = payload['remark']
    result = ProductHanlder.add_info(

        name=name,
        description=description,
        discount_id=discount_id,
        product_type_id=product_type_id,
        stock=stock,
        sale_price=sale_price,
        cost_price=cost_price,
        remark=remark,
    )
    return jsonify(result=result)

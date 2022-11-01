from flask import jsonify, request
from core.delivery_hanlder import DeliverHanlder
from app import app


@app.route('/delivery', methods=['POST'])
def add_delivery_info():
    payload = request.get_json()
    name = payload['name']
    price = payload['price']
    description = payload['description']
    remark = payload['remark']

    result = DeliverHanlder.add_info(
        name=name,
        price=price,
        description=description,
        remark=remark,

    )
    return jsonify(result=result)



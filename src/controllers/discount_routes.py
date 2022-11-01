from flask import request, jsonify
from core.discount_hanlder import DiscountHanlder
from app import app


@app.route('/discount', methods=['POST'])
def add_discount_info():
    payload = request.get_json()
    name = payload['name']
    price = payload['price']
    level_id = payload['level_id']
    open_date = payload['open_date']
    end_date = payload['end_date']
    is_active = payload['is_active']
    remark = payload['remark']
    result = DiscountHanlder.add_info(name=name, price=price, level_id=level_id, open_date=open_date, end_date=end_date,
                                      is_active=is_active, remark=remark)
    return jsonify(result=result)
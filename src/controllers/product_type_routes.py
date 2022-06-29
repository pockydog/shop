from flask import request, jsonify

from core.product_type_hanlder import ProductTypeHanlder
from app import app


@app.route('/product/type', methods=['GET'])
def get_product_type_info():
    """
    名稱查詢單筆資料
    """
    short_name = request.args.get('short_name')
    result = ProductTypeHanlder.get_info(short_name=short_name)
    return jsonify(result=result)


@app.route('/product/type', methods=['POST'])
def add_product_type_info():
    """
    新增資料
    """
    payload = request.get_json()
    name = payload['name']
    short_name = payload['short_name']
    code = payload['code']
    remark = payload['remark']
    result = ProductTypeHanlder.add_info(name=name, short_name=short_name, code=code, remark=remark)
    return jsonify(result=result)







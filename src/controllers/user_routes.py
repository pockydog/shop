from flask import request, jsonify
from app import app
from core.user_hanlder import UserHanlder


@app.route('/user', methods=['GET'])
def get_user_info():
    """
    名稱查詢單筆資料
    """
    phone_number = request.args.get('phone_number')
    result = UserHanlder.get_info(phone_number=phone_number)
    return jsonify(result=result)


@app.route('/user', methods=['POST'])
def add_user_info():
    """
    新增資料
    """
    payload = request.get_json()
    result = UserHanlder.add_info(
        name=payload['name'],
        account=payload['account'],
        password=payload['password'],
        phone_number=payload['phone_number'],
    )
    return jsonify(result=result)


@app.route('/user', methods=['DELETE'])
def del_user_info():
    """
    移除單筆資料
    """
    phone_number = request.args.get('phone_number')
    name = request.args.get('name')
    result = UserHanlder.del_info(name=name, phone_number=phone_number)
    return jsonify(result=result)


@app.route('/user', methods=['PUT'])
def update_user_info():
    """
    修改更新資料
    """
    payload = request.get_json()
    account = request.args.get('account')
    phone_number = payload['phone_number']
    password = payload['password']
    result = UserHanlder.update_info(account=account, phone_number=phone_number, password=password)
    return jsonify(result=result)


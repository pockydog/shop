from flask import request, jsonify
from app import app
from core.level_hanlder import LevelHanlder


@app.route('/level', methods=['GET'])
def get_level_info():
    """
    名稱查詢單筆資料
    """
    name = request.args.get('name')
    result = LevelHanlder.get_info(name=name)
    return jsonify(result=result)


@app.route('/level', methods=['POST'])
def add_level_info():
    """
    新增資料
    """
    result = LevelHanlder.add_info(name='VIP')
    return jsonify(result=result)


@app.route('/level', methods=['DELETE'])
def del_info():
    """
    移除資料
    """
    level_id = request.args.get('level_id')
    result = LevelHanlder.del_info(level_id == level_id)
    return jsonify(result=result)




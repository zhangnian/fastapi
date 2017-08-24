from flask import jsonify


def error_404_handler(error):
    resp = jsonify({'code': -1, 'msg': 'not found', 'data': None})
    resp.status_code = 404
    return resp


def error_429_handler(error):
    resp = jsonify({'code': -1, 'msg': 'to many requests', 'data': None})
    resp.status_code = 429
    return resp


def error_handler(error):
    response = jsonify(error.to_dict())
    return response
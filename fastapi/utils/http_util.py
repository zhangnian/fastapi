from flask import request, jsonify

from fastapi.utils.error import APIError


def render_ok(data=None):
    if data is None:
        data = {}
    return jsonify({'code': 0, 'msg': '', 'data': data})


def render_error(code, msg):
    assert code != 0
    return jsonify({'code': code, 'msg': msg, 'data': {}})


def get_qs_arg(name, parser=None, validator=None):
    val = request.args.get(name, None)
    if val is None:
        raise APIError(ret=1, msg='缺少参数:{}'.format(name))

    if parser and callable(parser):
        try:
            val = parser(val)
        except Exception as e:
            raise APIError(ret=1, msg='转换参数:{}失败'.format(name))

    if validator and callable(validator):
        if not validator(val):
            raise APIError(ret=1, msg='参数:{}不合法'.format(name))

    return val


def get_qs_arg_default(name, default=None, parser=None, validator=None):
    val = request.args.get(name, None)
    if val is None:
        if default is not None:
            return default
        raise APIError(ret=1, msg='缺少参数:{}'.format(name))

    if parser and callable(parser):
        try:
            val = parser(val)
        except Exception as e:
            raise APIError(ret=1, msg='转换参数:{}失败'.format(name))

    if validator and callable(validator):
        if not validator(val):
            raise APIError(ret=1, msg='参数:{}不合法'.format(name))

    return val


def get_json_arg(name, parser=None, validator=None):
    jdata = request.get_json(force=True, silent=True)

    if not request.is_json:
        raise APIError(ret=1, msg='请求数据格式错误')

    if jdata is None:
        raise APIError(ret=1, msg='请求数据格式错误')

    val = jdata.get(name, None)
    if val is None:
        raise APIError(ret=1, msg='缺少参数:{}'.format(name))

    if parser and callable(parser):
        try:
            val = parser(val)
        except Exception as e:
            raise APIError(ret=1, msg='转换参数:{}失败'.format(name))

    if validator and callable(validator):
        if not validator(val):
            raise APIError(ret=1, msg='参数:{}不合法'.format(name))
    return val


def get_json_arg_default(name, default=None, parser=None, validator=None):
    jdata = request.get_json(force=True, silent=True)

    if not request.is_json:
        raise APIError(ret=1, msg='请求数据格式错误')

    if jdata is None:
        raise APIError(ret=1, msg='请求数据格式错误')

    val = jdata.get(name, None)
    if val is None:
        if default is not None:
            return default
        raise APIError(ret=1, msg='缺少参数:{}'.format(name))

    if parser and callable(parser):
        try:
            val = parser(val)
        except Exception as e:
            raise APIError(ret=1, msg='转换参数:{}失败'.format(name))

    if validator and callable(validator):
        if not validator(val):
            raise APIError(ret=1, msg='参数:{}不合法'.format(name))
    return val
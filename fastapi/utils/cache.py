from flask import request


def user_cache_key():
    """从path paramaters中获取userid
    """
    return 'cache::user::{}'.format(request.view_args['id'])


def user_cache_key2():
    """从query string中获取userid
    """
    return 'cache::user::{}'.format(request.args['id'])


def user_cache_key3():
    """从json body中获取userid
    """
    return 'cache::user::{}'.format(request.json['id'])
"""
服务层
"""

from fastapi.model.user import User
from fastapi.fastapi import cache


def get_users():
    return User.query.all()


@cache.memoize()
def get_user_info(id):
    print('execute get_user_info...')
    return User.query.get_or_404(id)
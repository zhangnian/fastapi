from flask import abort, current_app, request, Blueprint
from fastapi.fastapi import cache
from fastapi.model.user import User, user_schema, users_schema
from fastapi.utils.http_util import render_ok, render_error
from fastapi.utils.cache import user_cache_key

bp = Blueprint("user", __name__, url_prefix='/user')


@bp.route('/users', methods=['GET'])
@cache.cached()
def users():
    users = User.query.all()
    if not users:
        abort(404)

    return users_schema.jsonify(users)


@bp.route('/users/<int:id>', methods=['GET'])
@cache.cached(key_prefix=user_cache_key)
def user(id):
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)


@bp.route('/user', methods=['POST'])
def add_user():
    # user, errors = user_schema.load(request.form)
    user, errors = user_schema.load(request.json)
    if errors:
        resp = render_error(code=1, msg='提交的数据不合法')
        resp.status_code = 400
        return resp

    user.save()
    resp = render_ok()
    resp.status_code = 201
    current_app.logger.info('add user success')
    return resp
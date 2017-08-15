from flask import abort, current_app, request
from fastapi.api.v1 import api_blueprint
from fastapi.model.user import User, user_schema, users_schema
from fastapi.utils.http_util import render_ok, render_error


@api_blueprint.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    if not users:
        abort(404)

    return users_schema.jsonify(users)


@api_blueprint.route('/users/<int:id>', methods=['GET'])
def user(id):
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)


@api_blueprint.route('/user', methods=['POST'])
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
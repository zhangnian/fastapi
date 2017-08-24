from flask import Blueprint

from fastapi.utils.http_util import render_ok
from fastapi.worker.tasks import async_add


bp = Blueprint("async", __name__, url_prefix='/async')


@bp.route('/add')
def add():
    future = async_add.delay(1, 2)
    return render_ok({'task_id': future.id})


@bp.route('/status/<task_id>')
def status(task_id):
    future = async_add.AsyncResult(task_id)

    if not future.ready():
        return render_ok({'status': 'pending'})

    return render_ok({'result': future.result})

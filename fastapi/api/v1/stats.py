from flask import Blueprint

from fastapi.fastapi import limiter
from fastapi.utils.stats import get_rps
from fastapi.utils.http_util import render_ok


bp = Blueprint("stats", __name__, url_prefix='/stats')


@bp.route('/rps')
@limiter.limit("3 per day")
def rps():
    data = {'qps': get_rps()}
    return render_ok(data)
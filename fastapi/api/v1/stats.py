from fastapi.api.v1 import api_blueprint
from fastapi.utils.stats import get_rps
from fastapi.utils.http_util import render_ok


@api_blueprint.route('/rps')
def rps():
    data = {'qps': get_rps()}
    return render_ok(data)
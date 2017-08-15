import time
from collections import deque

from flask import current_app


request_stats = deque()

def add_request():
    ts_now = int(time.time())

    # 只记录app.config['REQUEST_STATS_WINDOW']秒内的请求
    while len(request_stats) > 0 and request_stats[0] < (ts_now - current_app.config['REQUEST_STATS_WINDOW']):
        request_stats.popleft()

    request_stats.append(ts_now)


def get_rps():
    return '%.2f' % (len(request_stats) / current_app.config['REQUEST_STATS_WINDOW'])
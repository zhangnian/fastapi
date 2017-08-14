import redis

g_redis_client = None


def init_redis_client(app):
    host = app.config.get('REDIS_HOST')
    port = int(app.config.get('REDIS_PORT'))
    db = int(app.config.get('REDIS_DB'))
    password = app.config.get('REDIS_PASSWORD')

    global g_redis_client
    g_redis_client = redis.StrictRedis(host=host, port=port, db=db, password=password,
                                       socket_timeout=5, socket_connect_timeout=5)


def get_redis():
    global g_redis_client
    return g_redis_client
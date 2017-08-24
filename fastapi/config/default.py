
class Config:
    LOG_PATH = 'logs/'
    LOG_FILENAME = 'fastapi.log'
    LOG_LEVEL = 'info'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'

    ENABLE_SENTRY = False
    SENTRY_DSN = ''

    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = 'redis'

    REQUEST_STATS_WINDOW = 60

    BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
    CELERY_TASK_SERIALIZER = 'msgpack'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TASK_RESULT_EXPIRES = 60 * 60
    CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

    RATELIMIT_HEADERS_ENABLED = True

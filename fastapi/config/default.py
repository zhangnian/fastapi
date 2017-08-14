
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

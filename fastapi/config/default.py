
class Config:
    LOG_PATH = 'logs/'
    LOG_FILENAME = 'fastapi.log'
    LOG_LEVEL = 'info'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'

    ENABLE_SENTRY = False
    SENTRY_DSN = 'https://528bd615fd8e42beacf603d6270c99c8:6c4886cc414f4cd9b0045bfeeac3f1e5@sentry.io/127902'

    REDIS_HOST = 'r-bp1507482787ce14.redis.rds.aliyuncs.com'
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_PASSWORD = 'Jhy731005'

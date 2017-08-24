import time

from fastapi.fastapi import celery


@celery.task
def async_add(x, y):
    time.sleep(10)
    return x + y


from fastapi.utils.stats import add_request

def before_request_handler():
    add_request()


def after_request_handler(response):
    return response
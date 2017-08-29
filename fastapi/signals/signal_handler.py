from fastapi.fastapi import cache
from fastapi.utils.cache import user_cache_key


def on_userinfo_modify(sender):
    cache.delete(user_cache_key())


from flask import Blueprint


api_blueprint = Blueprint("api", __name__)

from fastapi.api.v1 import user
from fastapi.api.v1 import stats
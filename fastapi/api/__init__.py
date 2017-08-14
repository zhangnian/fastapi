from flask import Blueprint

api_blueprint = Blueprint("api", __name__)

from fastapi.api import user
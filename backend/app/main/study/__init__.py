from flask import Blueprint

study = Blueprint("study", __name__,url_prefix="/study")

from . import routes

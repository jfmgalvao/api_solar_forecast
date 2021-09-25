import json

from flask import Blueprint

routes = Blueprint('routes', __name__)

from .api_status_controller import api_status
from .forecast_controller import forecast_lstm


@routes.errorhandler(Exception)
def handle_exception(e):
    return json.dumps({"Error": str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

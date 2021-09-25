from logging import getLogger

from flask import request

from src.helpers.geopy_helper import get_location
from src.helpers.util import response_body
from src.models.payload_model import Payload
from src.services.collect_service import collect
from . import routes
from ..services.lstm_service import get_forecast_lstm

log = getLogger(__name__)


@routes.route('/forecast_lstm', methods=['POST'])
@response_body
def forecast_lstm():
    log.info('### start forecast ###')
    payload = Payload(**request.json)
    local = get_location(payload.address)

    df = collect(payload, local)
    result = get_forecast_lstm(df)
    log.info('### end forecast ###')

    return result.get_dict()

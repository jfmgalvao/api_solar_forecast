from src.helpers import STATUS_SUCCESS
from src.helpers.util import response_body
from . import routes


@routes.route('/api_status', methods=['GET'])
@response_body
def api_status():
    return {'status': STATUS_SUCCESS, 'message': 'API is running'}

from src.helpers.geopy_helper import get_location
from src.models.payload_model import Payload
from src.services.collect_service import collect


class TestCollect:
    def test_collect(self):
        payload = Payload('Avenida Vasco Rodrigues, 461 Peixinhos - Olinda PE', 2016, 2020)
        local = get_location(payload.address)

        df = collect(payload, local)
        assert df

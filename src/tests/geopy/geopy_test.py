from src.helpers.geopy_helper import get_location


class TestGeopy:
    def test_get_location(self):
        local = get_location('Avenida Vasco Rodrigues, 461 Peixinhos - Olinda PE')
        print(local.address)
        print(local.point)
        print(local.latitude)
        print(local.longitude)
        print(local.altitude)
        assert local

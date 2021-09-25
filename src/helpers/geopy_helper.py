from geopy.geocoders import Nominatim

from src.models.local_model import Local


def get_location(address):
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(address)

    return Local(location.address, location.point, location.latitude, location.longitude, location.altitude)

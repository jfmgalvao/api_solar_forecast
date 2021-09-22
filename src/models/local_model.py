class Local:
    def __init__(self, address, point, latitude, longitude, altitude):
        self.__address = address
        self.__point = point
        self.__latitude = latitude
        self.__longitude = longitude
        self.__altitude = altitude

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, v: str):
        self.__address = v

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, v):
        self.__point = v

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, v):
        self.__latitude = v

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, v):
        self.__longitude = v

    @property
    def altitude(self):
        return self.__altitude

    @altitude.setter
    def altitude(self, v):
        self.__altitude = v

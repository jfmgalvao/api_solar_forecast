class Payload:
    def __init__(self, address, start_year, end_year):
        self.__address = address
        self.__start_year = start_year
        self.__end_year = end_year

    @property
    def address(self):
        return self.__address

    @property
    def start_year(self):
        return self.__start_year

    @property
    def end_year(self):
        return self.__end_year

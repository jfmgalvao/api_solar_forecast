class Response:
    def __init__(self, status, rmse, mape, test_perdict, test_y):
        self.__status = status
        self.__rmse = rmse
        self.__mape = mape
        self.__test_predict = test_perdict
        self.__test_y = test_y

    @property
    def status(self):
        return self.__status

    @property
    def rmse(self):
        return self.__rmse

    @property
    def mape(self):
        return self.__mape

    @property
    def test_perdict(self):
        return self.__test_predict

    @property
    def test_y(self):
        return self.__test_y

    def get_dict(self):
        return {'status': self.__status, 'rmse': self.__rmse, 'mape': self.__mape,
                'test_perdict': self.__test_predict, 'test_y': self.__test_y}

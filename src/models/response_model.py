class Response:
    def __init__(self, status, train_rmse, test_rmse, mape, test_perdict, test_y, model):
        self.__status = status
        self.__train_rmse = train_rmse
        self.__test_rmse = test_rmse
        self.__mape = mape
        self.__test_predict = test_perdict
        self.__test_y = test_y
        self.__model = model

    @property
    def status(self):
        return self.__status

    @property
    def train_rmse(self):
        return self.__train_rmse

    @property
    def test_rmse(self):
        return self.__test_rmse

    @property
    def mape(self):
        return self.__mape

    @property
    def test_perdict(self):
        return self.__test_predict

    @property
    def test_y(self):
        return self.__test_y

    @property
    def model(self):
        return self.__model

    def get_dict(self):
        return {'status': self.__status, 'train_rmse': self.__train_rmse, 'test_rmse': self.__test_rmse,
                'mape': self.__mape, 'test_perdict': self.__test_predict, 'test_y': self.__test_y,
                'model': self.__model}

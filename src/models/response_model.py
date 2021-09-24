class Response:
    def __init__(self, status, train_score, test_score, mape, test_perdict, test_y):
        self.__status = status
        self.__train_score = train_score
        self.__test_score = test_score
        self.__mape = mape
        self.__test_predict = test_perdict
        self.__test_y = test_y

    @property
    def status(self):
        return self.__status

    @property
    def train_score(self):
        return self.__train_score

    @property
    def test_score(self):
        return self.__test_score

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
        return {'status': self.__status, 'train_score': self.train_score, 'test_score': self.__test_score,
                'mape': self.__mape, 'test_perdict': self.__test_predict, 'test_y': self.__test_y}

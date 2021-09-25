from logging import getLogger
from math import sqrt

import numpy as np
import pandas as pd
from keras.layers.core import Dense
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error

from src.helpers import STATUS_SUCCESS
from src.models.response_model import Response

log = getLogger(__name__)


def create_dataset(dataset, lb=30):
    data_x, data_y = [], []
    for i in range(len(dataset) - lb - 1):
        a = dataset[i:(i + lb), 0]
        data_x.append(a)
        data_y.append(dataset[i + lb, 0])
    return np.array(data_x), np.array(data_y)


def MAPE(y_true, y_pred):
    return np.mean(abs((y_true - y_pred) / y_true)) * 100


def build_model():
    # create and fit the LSTM network
    look_back = 30
    model = Sequential()
    model.add(LSTM(50, input_shape=(1, look_back)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')

    return model


def get_forecast_lstm(df):
    log.info('### start forcast lstm ###')

    df['date'] = df.index
    df['date'] = pd.to_datetime(df['date'])

    # normalized
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
    dataset = min_max_scaler.fit_transform(df['GHI'].values.reshape(-1, 1))

    # split into train and test sets
    df_length = len(dataset)
    train_limit = int(df_length / 2)
    validation_limit = train_limit + int((df_length - train_limit) / 2)
    train, val, test = dataset[0:train_limit], dataset[train_limit:validation_limit], dataset[validation_limit:]

    x_train, y_train = create_dataset(train, lb=30)
    x_val, y_val = create_dataset(val, lb=30)
    x_test, y_test = create_dataset(val, lb=30)

    # reshape
    x_train = np.reshape(x_train, (x_train.shape[0], 1, x_train.shape[1]))
    x_test = np.reshape(x_test, (x_test.shape[0], 1, x_test.shape[1]))
    x_val = np.reshape(x_val, (x_val.shape[0], 1, x_val.shape[1]))

    model = build_model()
    model_fited = model.fit(x_train, y_train, epochs=200, batch_size=1, validation_data=(x_val, y_val), verbose=0)

    train_predict = model.predict(x_train)
    test_predict = model.predict(x_test)
    # invert predictions
    train_predict = min_max_scaler.inverse_transform(train_predict)
    train_y = min_max_scaler.inverse_transform([y_train])
    test_predict = min_max_scaler.inverse_transform(test_predict)
    test_y = min_max_scaler.inverse_transform([y_test])
    # calculate root mean squared error
    train_rmse = sqrt(mean_squared_error(train_y[0], train_predict[:, 0]))
    test_rmse = sqrt(mean_squared_error(test_y[0], test_predict[:, 0]))
    log.debug(f'Train Score: {train_rmse:.2f} RMSE')
    log.debug(f'Test Score: {test_rmse:.2f} RMSE')

    mape = MAPE(test_y, test_predict)
    log.debug(f'MAPE: {mape:.2f}')

    log.info('### end forcast lstm ###')
    return Response(STATUS_SUCCESS, train_rmse, test_rmse, mape,
                    test_predict.reshape(-1).tolist(), test_y.reshape(-1).tolist(), model.to_json())

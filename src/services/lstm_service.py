import math

import numpy as np
import pandas as pd
from keras.layers.core import Dense
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from sklearn import preprocessing
# convert an array of values into a dataset matrix
from sklearn.metrics import mean_squared_error


def create_dataset(dataset, lb=30):
    dataX, dataY = [], []
    for i in range(len(dataset) - lb - 1):
        a = dataset[i:(i + lb), 0]
        dataX.append(a)
        dataY.append(dataset[i + lb, 0])
    return np.array(dataX), np.array(dataY)


def MAPE(y_true, y_pred):
    return np.mean(abs((y_true - y_pred) / y_true)) * 100


def get_best_result(df):
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

    # create and fit the LSTM network
    look_back = 30
    model = Sequential()
    model.add(LSTM(50, input_shape=(1, look_back)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model_fited = model.fit(x_train, y_train, epochs=200, batch_size=1, validation_data=(x_val, y_val), verbose=0)

    trainPredict = model.predict(x_train)
    testPredict = model.predict(x_test)
    # invert predictions
    trainPredict = min_max_scaler.inverse_transform(trainPredict)
    trainY = min_max_scaler.inverse_transform([y_train])
    testPredict = min_max_scaler.inverse_transform(testPredict)
    testY = min_max_scaler.inverse_transform([y_test])
    # calculate root mean squared error
    trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:, 0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:, 0]))
    print('Test Score: %.2f RMSE' % (testScore))

    predictRealInterval = min_max_scaler.inverse_transform(np.array(testPredict).reshape(1, -1))
    targetRealInterval = min_max_scaler.inverse_transform(y_test.reshape(1, -1))

    mape = MAPE(targetRealInterval, predictRealInterval)
    rmse = math.sqrt(mean_squared_error(targetRealInterval, predictRealInterval))
    print('MAPE: %.2f' % (mape))
    print('RMSE: %.2f' % (rmse))

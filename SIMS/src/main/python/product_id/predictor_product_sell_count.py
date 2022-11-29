import math
import matplotlib.pyplot as plt
import keras
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping
import csv

# read_File
sell_count = list()

product_id = ['PEA9_14800_3', 'PEA12_9980_2', 'PEA9_9980_6', 'PEA6_16800_3', 'PEA9_13400_3',
              'PEA5_11400_1', 'PEA10_13800_2', 'PEA11_14800_3', 'PEA4_8400_1', 'PEA3_9800_1',
              'PEA8_13400_2', 'PEA9_13800_1', 'PEA4_13800_1', 'PEA7_13800_2', 'PEA14_16800_2',
              'PEA9_7480_2', 'PEA9_15800_2', 'PEA12_14800_2', 'PEA7_10800_1', 'PEA7_11040_1',
              'PEA8_19800_2', 'PEA10_13400_1', 'PEA9_10400_3', 'PEA9_13800_2', 'PEA6_14800_2',
              'PEA10_19800_1', 'PEA7_8980_1', 'PEA9_10980_6', 'PEA9_7980_4', 'PEA8_6980_3']

for i in range(30):
    sell_count = list()
    with open(f'product/{product_id[i]}.csv', 'r', encoding='cp949', newline='') as file:
        rdr = csv.reader(file)
        for idx, line in enumerate(rdr):
            if idx == 0:
                continue
            line = ''.join(line)
            line = int(line)
            sell_count.append(line)
    # 딥러닝 모델에 대입하기 위해 형태를 바꿔준다.

    print(sell_count)

    # Normalization => 정규화
    sell_count = np.asarray(sell_count)
    sell_count_max = max(sell_count)
    sell_count_min = min(sell_count)
    sell_count = ((sell_count-sell_count_min)/(sell_count_max-sell_count_min))
    print(sell_count_max, sell_count_min)

    # print(price)
    # exit()

    seq_len = 5 # 최근 10일에 데이터

    # +1이므로 다음날 하루 예측
    sequence_length = seq_len + 1
    # 10일에 데이터를 가지고 하루를 예측한다 했으므로, 전체 데이터를 11개씩 짤라준다.
    result = []
    for index in range(len(sell_count)-sequence_length):
        result.append(sell_count[index:index+sequence_length])

    # 정규화 부분인데, 위에 이미 진행해서 normalized_data 리스트에만 담아줘도 된다.
    normalized_data = []

    for window in result:
        normalized_data.append(window)
    result = np.array(normalized_data)

    # train data와 validation data를 8:2으로 나눈다.
    row = int(round(result.shape[0]*0.8))
    train = result[:row,:]
    np.random.shuffle(train)

    x_train = train[:,:-1]
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    y_train = train[:,-1]

    x_test = result[row:,:-1]
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    y_test = result[row:,-1]


    # LSTM (Long Short Term Memory)
    model = Sequential()

    # input : 10, 10일을 사용
    model.add(LSTM(5, activation='relu', return_sequences = True, input_shape=(5,1)))

    model.add(LSTM(12, return_sequences = False))

    # output : 1, 1일 예측
    model.add(Dense(1))

    model.summary()

    # 평균 제곱 오차, LSTM에서 주로 사용된다.
    model.compile(
        optimizer='adam',
        loss='mse',
    )

    model.fit(x_train, y_train,
              validation_data=(x_test, y_test),
              batch_size=1,
              epochs=15
            )

    model.save(f'predictor_{product_id[i]}_sell_weight.h5')

    preds = model.predict(x_test)
    pred = preds[-1]
    print(preds[-1])

    print("Normalized predicted value : ", round(float(pred), 2))
    result = pred * (sell_count_max-sell_count_min)

    print(f"Predicted '{product_id[i]}' sell count :", int(result))

    fig = plt.figure(facecolor = 'white')
    ax = fig.add_subplot(111)
    ax.plot((y_test*(sell_count_max-sell_count_min)), label = 'True')
    ax.plot((preds*(sell_count_max-sell_count_min)), label='Prediction')
    ax.legend()
    plt.show()

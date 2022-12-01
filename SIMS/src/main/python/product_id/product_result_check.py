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
import pymysql
import csv
from keras.models import load_model

def product(conn, tel):
    
    cur = conn.cursor()
    cur.execute("SELECT productCode FROM product")
    products = cur.fetchall()
    for product in products:
        print('product_id/predictor_' + product[0] + '_sell_weight.h5')
        model = load_model('product_id/predictor_' + product[0] + '_sell_weight.h5')
        print(tel)
        model.summary()

        # 평균 제곱 오차, LSTM에서 주로 사용된다.
        model.compile(
            optimizer='adam',
            loss='mse',
        )

        cur.execute("SELECT sales FROM productSales WHERE name='" + product[0] + "' and tel='" + tel + "' ORDER BY date;")
        rows = cur.fetchall()
        for row in rows:
            price.append(row[0])
        # # read_File
        # price = list()
        # with open('product/' + product + '.csv', 'r', encoding='cp949', newline='') as file:
        #     rdr = csv.reader(file)
        #     file.readline()
        #     for line in rdr:
        #         print(line)
        #         line = ''.join(line)
        #         line = int(line)
        #         price.append(line)
        # 딥러닝 모델에 대입하기 위해 형태를 바꿔준다.
        # Normalization => 정규화
        price = np.asarray(price)
        price_max = max(price)
        price_min = min(price)
        price = ((price-price_min)/(price_max-price_min))
        # print(price_max, price_min)

        # print(price)
        # exit()

        seq_len = 5 # 최근 10일에 데이터

        # +1이므로 다음날 하루 예측
        sequence_length = seq_len + 1
        # 10일에 데이터를 가지고 하루를 예측한다 했으므로, 전체 데이터를 11개씩 짤라준다.
        result = []
        for index in range(len(price)-sequence_length):
            result.append(price[index:index+sequence_length])

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

        # Predict
        preds = model.predict(x_test)
        pred = preds[-1]
        # print(preds[-1])

        print("prediction rate : ", round(float(pred * 100), 2), "%")
        result = pred * (price_max-price_min)
        result = int(result)

        print("Predicted Day income :", result)

        cur.execute("SELECT * FROM productPredict WHERE name=" + product[0] + " and tel='" + tel + "';")
        row = cur.fetchone()
        if (row == None):
            cur.execute("INSERT INTO productPredict VALUES(NULL, '" + str(result) + "', '" + tel + "', name='" + product[0] + "');")
        else:
            cur.execute("UPDATE productPredict SET predict=" + str(result) + " WHERE tel='" + tel +"' and name='" + product[0] + "';")
        conn.commit()
        # # 파일 Data 추가
        # with open('product_id/product_predicted.csv', 'a', encoding='cp949', newline='') as file:
        #     result_str = str(result)
        #     file.write(result_str)


        # fig = plt.figure(facecolor = 'white')
        # ax = fig.add_subplot(111)
        # ax.plot(y_test,label = 'True')
        # ax.plot(preds, label='Prediction')
        # ax.legend()
        # plt.show()

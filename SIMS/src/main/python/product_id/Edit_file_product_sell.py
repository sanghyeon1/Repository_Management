#-*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import csv

df1 = pd.read_csv('account_log_sorted_item.csv', encoding='cp949')
df2 = pd.read_csv('account_log_totalincome.csv', encoding='cp949')
print(df1.shape)

sell_price = df1['원가']
sell_p = df1['판매가격']
sell_count = df1['판매량']
product_name = df1['재품명'][0]

print(sell_count[1])
print(len(df1))
# exit()

sell_count_list = [[] for _ in range(30)]

cnt = 0

for i in range(len(df1)):
    if df1['재품명'][i] == product_name:
        if sell_price[i] == 0:
            if sell_p[i] != 0:
                sell_count_list[cnt].append(sell_count[i])

    elif df1['재품명'][i] != product_name:
        cnt += 1
        product_name = df1['재품명'][i]

        if sell_price[i] == 0:
            if sell_p[i] != 0:
                sell_count_list[cnt].append(sell_count[i])

print(sell_count_list[0])

for i in range(len(sell_count_list)):
    print(len(sell_count_list[i]))


product_id = ['PEA9_14800_3', 'PEA12_9980_2', 'PEA9_9980_6', 'PEA6_16800_3', 'PEA9_13400_3',
              'PEA5_11400_1', 'PEA10_13800_2', 'PEA11_14800_3', 'PEA4_8400_1', 'PEA3_9800_1',
              'PEA8_13400_2', 'PEA9_13800_1', 'PEA4_13800_1', 'PEA7_13800_2', 'PEA14_16800_2',
              'PEA9_7480_2', 'PEA9_15800_2', 'PEA12_14800_2', 'PEA7_10800_1', 'PEA7_11040_1',
              'PEA8_19800_2', 'PEA10_13400_1', 'PEA9_10400_3', 'PEA9_13800_2', 'PEA6_14800_2',
              'PEA10_19800_1', 'PEA7_8980_1', 'PEA9_10980_6', 'PEA9_7980_4', 'PEA8_6980_3']

for i in range(30):
    a = sell_count_list[i]
    df3 = pd.DataFrame(a, columns=[product_id[i]])
    df3[f'{product_id[i]}'].to_csv(f"./product_id/{product_id[i]}.csv", index=False)

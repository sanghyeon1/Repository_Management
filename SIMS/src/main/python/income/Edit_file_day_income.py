#-*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import csv

total_day_account = []

df1 = pd.read_csv('account_log_all.csv', encoding='cp949')
df2 = pd.read_csv('account_log_totalincome.csv', encoding='cp949')
print(df1.shape)

current_day = df1['판매날짜'][0]

print(current_day)

cnt = 0
for idx, day in enumerate(df1['판매날짜']):
    if current_day != day:
        print(day)
        total_day_account.append(df2['ACCOUNT_TOTAL'][idx-1])
        current_day = day

print(len(total_day_account))
print(total_day_account[0:5])

with open('account_day_total.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(map(lambda x: [x], total_day_account))


        

import csv
import random

from collections import deque
import pandas as pd
import stock_system_data_input as sdi
'''
FINANCIAL
- telnumber  # 사용자 식별 primary key
- income  # 수입(정수)
- spend  # 지출(정수)
- amount # 수입 또는 지출된 양
- date  # 수입 또는 지출 날짜(yyyy-mm-dd)
- product_id  # 상품아이디(foriegn key)
- stored  # 저장된 재고량
- expiration  # 유통기한(입고 후 5일까지)
- total_cost  # 총 금액(정수)
'''
product_id = ['PEA9_14800_3', 'PEA12_9980_2', 'PEA9_9980_6', 'PEA6_16800_3', 'PEA9_13400_3',
              'PEA5_11400_1', 'PEA10_13800_2', 'PEA11_14800_3', 'PEA4_8400_1', 'PEA3_9800_1',
              'PEA8_13400_2', 'PEA9_13800_1', 'PEA4_13800_1', 'PEA7_13800_2', 'PEA14_16800_2',
              'PEA9_7480_2', 'PEA9_15800_2', 'PEA12_14800_2', 'PEA7_10800_1', 'PEA7_11040_1',
              'PEA8_19800_2', 'PEA10_13400_1', 'PEA9_10400_3', 'PEA9_13800_2', 'PEA6_14800_2',
              'PEA10_19800_1', 'PEA7_8980_1', 'PEA9_10980_6', 'PEA9_7980_4', 'PEA8_6980_3']

name = ['감바스 알 아히요', '모짜렐라 로제누들떡볶이', '샤브샤브 요리재료', '밀푀유 나베', '차돌박이 숙주볶음',
        '초마 짬뽕', '쉬림프 로제 파스타', '오사카식 오코노미야키', '마파두부', '짜장면',
        '리북방 순대전골', '까르보나라 파스타', '쫄면무침', '소불고기 전골', '얼큰미나리 샤브샤브 칼국수',
        '닭볶음탕 요리재료', '오사카식 야키소바', '베트남식 소고기 쌀국수', '매콤 순대볶음', '광동식 탄탄면',
        '일호식 스키야키', '신림동식 백순대볶음', '우삼겹 순두부찌개', '푸짐한 대구매운탕', '푸짐한 알탕',
        '한우 차돌 된장찌개', '영월식 청국장', '어메이징 부대찌개', '의정부식 부대찌개', '원주식 장칼국수']

# 삼차원 리스트 : 1차원(년) : 0, 1 // 2차원(월) : 0 ~ 11 // 3차원(일) : 그 해의 날 수
date = sdi.get_date()

m = []
for k in range(12):
    print(len(date[0][k]))
    for i in range(len(date[0][k])):
        a = []
        for j in range(30):
            if k//4==0:
                a.append(int(round(random.uniform(0, 4) * sdi.popularity1[j], 0)))
            elif k//4==1:
                a.append(int(round(random.uniform(0, 4) * sdi.popularity2[j], 0)))
            elif k//4==2:
                a.append(int(round(random.uniform(0, 4) * sdi.popularity3[j], 0)))
            else:
                a.append(int(round(random.uniform(0, 4) * sdi.popularity4[j], 0)))
        m.append(a)
for k in range(12):
    for i in range(len(date[1][k])):
        a = []
        for j in range(30):
            if k // 4 == 0:
                a.append(int(round(random.uniform(0, 4) * sdi.popularity1[j], 0)))
            elif k // 4 == 1:
                a.append(int(round(random.uniform(0, 4) * sdi.popularity2[j], 0)))
            elif k // 4 == 2:
                a.append(int(round(random.uniform(0, 4) * sdi.popularity3[j], 0)))
            else:
                a.append(int(round(random.uniform(0, 4) * sdi.popularity4[j], 0)))
        m.append(a)

# m : 2차원 리스트, 2021년도 판매 데이터. 각 행은 일자(총 365개), 행 내 데이터는 각 항목(30개) 당 판매 개수.

telnumbers = [] #파일로부터 유저 불러와서 telnumber 뽑아서 리스트화
user = pd.read_csv('USERS.csv')
for i in range(len(user)):
    telnumbers.append(user.iloc[i,3])

def financial(m):
    # 11월 17일 : income, spend, date, product_id, stored 구현 완료.
    global product_id, name
    # stored = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
    #           30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
    #           30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
    stored = [30 for _ in range(30)]
    stored_bak = stored.copy()
    refill_period = [0 for _ in range(len(stored))]
    price = [14800, 9980, 9980, 16800, 13400, 11400, 13800, 14800, 8400, 9800,
             13400, 13800, 13800, 13800, 16800, 7480, 15800, 14800, 10800, 11040,
             19800, 13400, 10400, 13800, 14800, 19800, 8980, 10980, 7980, 6980]
    # 마진은 40%
    cost_rate = 0.6
    del_count = 0
    expiration_list = deque()

    date_flat = [x for y in date for x in y]
    date_flat = [x for y in date_flat for x in y]
    date_fin_list = list(reversed(date_flat))
    # sold_amount = [0 for _ in range(30)]
    over_amount = [0 for _ in range(30)]
    total_cost = 0
    line = []
    for i in range(30):
        total_cost -= int(price[i] * stored[i] * cost_rate)
        line.append([telnumbers[0], 0, price[i]*cost_rate, stored[i], '2020-1-1', product_id[i], stored[i], '2020-1-6',
                     total_cost])
        expiration_list.append(['2020-1-6', i, stored[i]])
    for i in range(len(m)):  # 731 날짜
        date_fin = date_fin_list.pop()
        if expiration_list:
            while expiration_list[0][0] == date_fin:
                popitem = expiration_list.popleft()
                # if popitem[1] == 21:
                #     print(product_id[popitem[1]], popitem[0], popitem[2], stored[popitem[1]])
                over_amount[popitem[1]] = popitem[2]
                stored[popitem[1]] -= popitem[2]
                line.append([telnumbers[0], 0, 0, popitem[2], date_fin, product_id[popitem[1]], stored[popitem[1]], 0,
                             total_cost])
                del_count += 1
        year, month, day = map(int, date_fin.split('-'))
        day += 5
        if year == 2020 and month == 2 and day > 29:
            month += 1
            day -= 29
        elif month == 2 and day > 28:
            month += 1
            day -= 28
        elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
            month += 1
            day -= 30
        elif day > 31:
            month += 1
            day -= 31
        if month > 12:
            year += 1
            month -= 12
        expiration = str(year) + '-' + str(month) + '-' + str(day)
        for j in range(len(m[i])):  # 30 품목
            refill_period[j] += 1
            amount = m[i][j]
            if amount == 0:
                continue
            # sold_amount[j] += amount
            income = price[j]
            # spend = int(cost_rate * income)
            product_id_fin = product_id[j]
            # stored[j] -= amount
            if stored[j] != 0:
                if stored[j] - amount < 0:
                    amount = stored[j]
                    stored[j] = 0
                else:
                    stored[j] -= amount
                total_cost += int(amount * income)
                line.append([telnumbers[0], income, 0, amount, date_fin, product_id_fin, stored[j], 0,
                             total_cost])
            # amount_bak = amount
            idx = 0
            for k in expiration_list:
                idx += 1
                if k[1] == j:
                    if k[2] > amount:
                        k[2] -= amount
                        break
                    else:
                        amount -= k[2]
                        k[2] = 0
            if stored[j] < (stored_bak[j]*0.2):
                if over_amount[j] != 0:
                    if stored_bak[j] > (over_amount[j] + 10):
                        stored_bak[j] -= over_amount[j]
                    else:
                        stored_bak[j] = 10
                    # if (stored_bak[j] - over_amount[j]) > 20:
                    #     if over_amount[j] <= 15:
                    #         stored_bak[j] = int(stored_bak[j] - over_amount[j])
                        # else:
                        #     stored_bak[j] = 15
                    over_amount[j] = 0
                    # refill_period[j] = 0
                else:
                    stored_bak[j] = int(stored_bak[j] * (5 / refill_period[j]))
                stored[j] += stored_bak[j]
                spend = int(cost_rate * price[j])
                total_cost -= spend * stored_bak[j]
                line.append([telnumbers[0], 0, spend, stored_bak[j], date_fin, product_id_fin, stored[j], expiration,
                             total_cost])

                # storedj_bak = stored_bak[j]
                # for k in expiration_list:
                #     if k[1] == j and k[2] >= storedj_bak:
                #         k[2] -= storedj_bak
                #         break
                #     elif k[1] == j and k[2] < storedj_bak:
                #         storedj_bak -= k[2]
                #         k[2] = 0

                expiration_list.append([expiration, j, stored_bak[j]])
                refill_period[j] = 0

    # df3 = pd.DataFrame(ID, columns=['ID'])
    # df3['password'] = password
    # df3['username'] = username
    print(del_count)
    print(stored_bak)
    return line

accountlog = financial(m)
with open('account_log_all.csv', 'w', newline='') as wf:
    writer = csv.writer(wf)
    writer.writerows(accountlog)

accountlog2 = sorted(accountlog,key=lambda x:x[5])
with open('account_log_sorted_item.csv', 'w', newline='') as wf:
    writer = csv.writer(wf)
    writer.writerows(accountlog2)
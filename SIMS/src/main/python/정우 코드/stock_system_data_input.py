import random as rn
import pandas as pd

# stock DB .csv

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

price = [14800, 9980, 9980, 16800, 13400, 11400, 13800, 14800, 8400, 9800,
         13400, 13800, 13800, 13800, 16800, 7480, 15800, 14800, 10800, 11040,
         19800, 13400, 10400, 13800, 14800, 19800, 8980, 10980, 7980, 6980]

popularity1 = [3, 2, 6, 3, 3, 1, 2, 3, 1, 1,
              2, 1, 1, 2, 2, 2, 2, 2, 1, 1,
              2, 1, 3, 2, 2, 1, 1, 6, 4, 3]

popularity2 = [2,4,1,2,1,2,2,1,1,3,4,2,1,3,1,2,1,1,1,3,2,2,3,2,4,4,6,3,5,4]

popularity3 = [1,2,3,2,1,1,2,2,2,2,1,2,4,2,1,2,3,3,2,1,3,1,1,1,2,1,5,4,6,3]

popularity4 = [2,1,1,3,3,2,1,1,1,3,3,1,2,3,2,1,5,2,1,3,2,2,1,3,1,3,2,5,4,3]


def make_codes():
    # 코드 구성:
    # 상품회사(PEACOCK 에서 PEA만 따옴.)_상품이름의 길이(공백 포함.)_가격_인기도.
    global name, price, popularity1, popularity2, popularity3, popularity4
    code = []
    pro_company = 'PEA'

    for i in range(len(name)):
        temp = pro_company + str(len(name[i])) + '_' + str(price[i]) + '_' + str(popularity[i])
        code.append(temp)
    print(code)
    return code


def get_stored_num():
    stored = []
    num = 0
    for i in range(len(popularity1)):
        num = (round((popularity1[i] / 2)) * 5) + 100
        stored.append(int(num))
    # print(stored)
    return stored


def get_date():
    # 2020년도 2월 : 29일
    # 2021년도 2월 : 28일
    # 1월: 31일 2월:28/29일 3월:31일 4월:30일 5월:31일 6월:30일 7월:31일 8월:31일 9월:30일 10월:31일 11월:30일 12월:31일
    years = [2020, 2021]
    month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    total_date = []
    for year in years:
        month_day = []
        for mon in month:
            dates = []
            if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
                for k in range(1, 32):
                    date = str(year) + '-' + str(mon) + '-' + str(k)
                    dates.append(date)
            if year == 2020 and mon == 2:
                for l in range(1, 30):
                    date = str(year) + '-' + str(mon) + '-' + str(l)
                    dates.append(date)
            if year == 2021 and mon == 2:
                for m in range(1, 29):
                    date = str(year) + '-' + str(mon) + '-' + str(m)
                    dates.append(date)
            if mon == 4 or mon == 6 or mon == 9 or mon == 11:
                for n in range(1, 31):
                    date = str(year) + '-' + str(mon) + '-' + str(n)
                    dates.append(date)
            month_day.append(dates)
        total_date.append(month_day)
    # for i in range(len(total_date)):
    #     for j in range(len(total_date[i])):
    #         cnt += len(total_date[i][j])

    # print(f"{total_date}")
    return total_date


def output_to_csv(df, num):
    if num == 1:
        return df.to_csv(f"PRODUCT.csv", index=False)
    elif num == 2:
        return df.to_csv(f"STOCK.csv", index=False)
    elif num == 3:
        return df.to_csv(f"USERS.csv", index=False)


def main():
    df = pd.DataFrame(product_id, columns=['product_id'])
    df['name'] = name
    df['price'] = price
    df['popularity'] = popularity1
    # print(df)
    output_to_csv(df, 1)
    stored = get_stored_num()

    released = [0 for _ in range(30)]
    amount = [0 for _ in range(30)]
    date = get_date()  # 삼차원 리스트 : 1차원 : 0, 1 // 2차원 : 0 ~ 11 // 3차원 : 그 해의 날 수

    df2 = pd.DataFrame(stored, columns=['stored'])
    df2['product_id'] = product_id
    df2['amount'] = stored
    df2['date'] = [date[0][0][0] for _ in range(30)]
    df2['expiration'] = [date[0][0][5] for _ in range(30)]
    # print(df2)

    # two_dimension_list = []
    # for i in range(len(stored)):
    #     amount[i] = amount[i]
    #     lists = [stored[i], product_id[i], amount[i]]
    #
    # for i in range(1, 13):
    #     df3 = pd.DataFrame([[], []])
    # df4 = pd.DataFrame(stored, columns=['stored'])
    output_to_csv(df2, 2)

    ID = ['psh990429', 'daun5696', 'kirigaya0']
    username = ['박상현', '정다은', '양지웅']
    password = ['qkrtkdgus123', 'wjdekdms456', 'didwldnd789']
    telnumber = ['010-6324-4435', '010-9057-5449', '010-9456-8472']

    df3 = pd.DataFrame(ID, columns=['ID'])
    df3['password'] = password
    df3['username'] = username
    df3['telnumber'] = telnumber
    output_to_csv(df3, 3)
    # df2['date'] = get_date()


main()
"""
    - ID
    - username
    - password
    - telnumber


    - telnumber
    - income
    - spend
    - date
    - product_id
    - amount
1. 감바스 알 아히요 - 14,800 - 3줄
2. 모짜렐라 로제누들떡볶이 - 9,980 - 2줄
3. 샤브샤브 요리재료 - 9,980 - 6줄
4. 밀푀유 나베 - 16,800 - 3줄
5. 차돌박이 숙주볶음 - 13,400 - 3줄
6. 초마 짬뽕 -  11,400 - 1줄
7. 쉬림프 로제 파스타 - 13,800 - 2줄
8. 오사카식 오코노미야키 - 14,800 - 3줄
9. 마파두부 - 8,400 - 1줄
10. 짜장면 - 9,800 - 1줄
11. 리북방 순대전골 - 13,400 - 2줄
12. 까르보나라 파스타 - 13,800 - 1줄
13. 쫄면무침 - 13,800 - 1줄
14. 소불고기 전골 - 13,800 - 2줄
15. 얼큰미나리 샤브샤브 칼국수 - 16,800 - 2줄
16. 닭볶음탕 요리재료 - 7,480 - 2줄
17. 오사카식 야키소바 - 15,800 - 2줄
18. 베트남식 소고기 쌀국수 - 14,800 - 2줄
19. 매콤 순대볶음 - 10,800 - 1줄
20. 광동식 탄탄면 - 11,040 - 1줄
21. 일호식 스키야키 - 19,800 - 2줄
22. 신림동식 백순대볶음 - 13,400 - 1줄
23. 우삼겹 순두부찌개 - 10,400 - 3줄
24. 푸짐한 대구매운탕 - 13,800 - 2줄
25. 푸짐한 알탕 - 14,800 - 2줄
26. 한우 차돌 된장찌개 - 19,800 - 1줄
27. 영월식 청국장 - 8,980 - 1줄
28. 어메이징 부대찌개 - 10,980 - 6줄
29. 의정부식 부대찌개 - 7,980 - 4줄
30. 원주식 장칼국수 - 6,980 - 3줄

"""
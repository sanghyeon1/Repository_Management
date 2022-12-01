import pymysql
import pandas as pd

def memberInsert(conn):
    df = pd.read_csv('inserts/member.csv')
    item_list = df[['user_id', 'name', 'password', 'tel']]

    conn = pymysql.connect(host='127.0.0.1', user='root', db='SIMS', charset='utf8')
    cur = conn.cursor()
    row_count, column_count = df.shape

    for i in range(0, row_count):
        cur.execute('INSERT INTO member VALUES ("'
                + str(item_list.iloc[i]['user_id']) + '", "' 
                + str(item_list.iloc[i]['name']) + '", "' 
                + str(item_list.iloc[i]['password']) + '", "' 
                + str(item_list.iloc[i]['tel'])
                + '" );')

    conn.commit()
    print("member insert 성공")
    # conn.close()
import pymysql
import pandas as pd

def productInsert():
    df = pd.read_csv('inserts/product.csv')
    item_list = df[['name', 'price', 'productCode']]

    conn = pymysql.connect(host='127.0.0.1', user='root', db='SIMS', charset='utf8')
    cur = conn.cursor()
    row_count, column_count = df.shape

    for i in range(0, row_count):
        cur.execute('INSERT INTO product VALUES (NULL, ' + '"'
                + str(item_list.iloc[i]['name']) + '", "' 
                + str(item_list.iloc[i]['price']) + '", "' 
                + str(item_list.iloc[i]['productCode']) + '", "' 
                + str(int(item_list.iloc[i]['price'] * 0.6)) + '" );')

    conn.commit()
    print("product insert 성공")
    conn.close()
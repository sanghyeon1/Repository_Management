import pymysql

def productSalesInsert():
    conn = pymysql.connect(host='127.0.0.1', user='root', db='SIMS', password='1234', charset='utf8')
    cur = conn.cursor()

    cur.execute('SELECT * FROM log WHERE type="sell"')

    rows = cur.fetchall()

    for row in rows:
        cur.execute('INSERT INTO productSales VALUES (NULL, '
                + str(row[3]) + ', "' 
                + str(row[2]) + '", "' 
                + str(row[1]) + '" );')
        
    conn.commit()
    print("product sales insert 성공")
    conn.close()
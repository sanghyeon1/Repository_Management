from inserts import accountInsert
from inserts import logInsert
from inserts import memberInsert
from inserts import productInsert
from inserts import productSalesInsert
from inserts import productStockInsert
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='SIMS', charset='utf8')

logInsert.logInsert(conn)
memberInsert.memberInsert(conn)
productInsert.productInsert(conn)
accountInsert.accountInsert(conn)
productSalesInsert.productSalesInsert(conn)
productStockInsert.productStockInsert(conn)

conn.close()
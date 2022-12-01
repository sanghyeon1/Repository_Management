from inserts import accountInsert
from inserts import logInsert
from inserts import memberInsert
from inserts import productInsert
from inserts import productSalesInsert
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', db='SIMS', charset='utf8')

logInsert.logInsert(conn);
memberInsert.memberInsert(conn);
productInsert.productInsert(conn);
accountInsert.accountInsert(conn);
productSalesInsert.productSalesInsert(conn);

conn.close()
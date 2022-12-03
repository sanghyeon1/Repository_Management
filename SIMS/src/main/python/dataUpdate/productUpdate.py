import pymysql

def productSalesUpdate(conn, tel):
	# conn = pymysql.connect(host='127.0.0.1', user='root', db='SIMS', charset='utf8')
	cur = conn.cursor()

	cur.execute("DELETE FROM productSales WHERE tel='" + tel + "';")

	cur.execute('SELECT * FROM log WHERE type="sell" and tel=\'' + tel + "';")

	rows = cur.fetchall()

	for row in rows:
		cur.execute('INSERT INTO productSales VALUES (NULL, '
				+ str(row[3]) + ', "' 
				+ str(row[2]) + '", "'
				+ str(row[1]) + '", "'
				+ str(row[4]) + '" );')
		
	conn.commit()
	print("product sales update 성공")
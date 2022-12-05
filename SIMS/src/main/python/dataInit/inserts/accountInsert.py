import pymysql

def accountInsert(conn):
	# conn = pymysql.connect(host='127.0.0.1', user='root', db='SIMS', charset='utf8')
	cur = conn.cursor()

	cur.execute("SELECT date, sum(amount*p.primeCost) FROM log as l, product as p WHERE type='buy' and l.productCode=p.productCode group by date order by date;")
	spends = cur.fetchall()

	cur.execute("SELECT date, sum(amount*p.price) FROM log as l, product as p WHERE type='sell' and l.productCode=p.productCode group by date order by date;")
	incomes = cur.fetchall()


	i = 0
	sum = 0;
	for income in incomes:
		money = income[1]
		if income[0] == spends[i][0]:
			money -= spends[i][1]
			i += 1
		sum += money
		cur.execute('INSERT INTO account VALUES (NULL, '
				+ str(sum) + ', "' 
				+ str("010-6324-4435") + '", "' 
				+ str(income[0]) + '" );')

	conn.commit()
	print("account insert 성공")
	# conn.close()
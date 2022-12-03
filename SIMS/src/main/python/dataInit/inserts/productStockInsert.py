import pymysql

def productStockInsert(conn):
	cur = conn.cursor()
 
	cur.execute("SELECT productCode, sum(amount), tel FROM log WHERE type='buy' and tel='010-6324-4435' group by productCode;")
	spends = cur.fetchall()
	cur.execute("SELECT productCode, sum(amount), tel FROM log WHERE type='sell' and tel='010-6324-4435' group by productCode;")
	incomes = cur.fetchall()
	cur.execute("SELECT productCode, sum(amount), tel FROM log WHERE type='disposal' and tel='010-6324-4435' group by productCode;")
	disposals = cur.fetchall()
	cur.execute("select productCode from product")
	products = cur.fetchall()

	for product in products:
		amount = 0
		for spend in spends:
			if (spend[0] == product[0]):
				amount += spend[1]
				break
		for income in incomes:
			if (income[0] == product[0]):
				amount -= income[1]
				break
		for disposal in disposals:
			if (disposal[0] == product[0]):
				amount -= disposal[1]
				break
		cur.execute("SELECT * FROM productStock WHERE tel='010-6324-4435' and productCode='" + product[0] + "';")
		row = cur.fetchone()
		if (row == None):
			cur.execute('INSERT INTO productStock VALUES (NULL, "'
				+ str(product[0]) + '", "' 
				+ str('010-6324-4435') + '", "' 
				+ str(amount) + '" );')
		else:
			cur.execute("UPDATE productStock SET amount=" + str(amount) + " WHERE tel='010-6324-4435';")
	conn.commit()
	print("product stock update 성공")
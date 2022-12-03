import pymysql

def productStockUpdate(conn, tel):
	cur = conn.cursor()
 
	cur.execute("DELETE FROM productStock WHERE tel='" + tel + "';")
 
	cur.execute("SELECT productCode, sum(amount), tel FROM log WHERE type='buy' and tel='" + tel + "' group by productCode;")
	spends = cur.fetchall()
	cur.execute("SELECT productCode, sum(amount), tel FROM log WHERE type='sell' and tel='" + tel + "' group by productCode;")
	incomes = cur.fetchall()
	cur.execute("select productCode from product")
	products = cur.fetchall()

	for product in products:
		print(product[0])
		amount = 0
		for spend in spends:
			if (spend[0] == product[0]):
				amount += spend[1]
				tel = spend[2]
				break
		for income in incomes:
			if (income[0] == product[0]):
				amount -= income[1]
				tel = spend[2]
				break
		cur.execute("SELECT * FROM productStock WHERE tel='" + tel + "' and productCode='" + product[0] + "';")
		row = cur.fetchone()
		if (row == None):
			cur.execute('INSERT INTO productStock VALUES (NULL, "'
				+ str(product[0]) + '", "' 
				+ str(tel) + '", "' 
				+ str(amount) + '" );')
		else:
			cur.execute("UPDATE productStock SET amount=" + str(amount) + " WHERE tel='" + tel + "';")
	conn.commit()
	print("product stock update 성공")
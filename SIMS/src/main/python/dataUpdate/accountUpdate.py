import pymysql
from datetime import datetime

def accountUpdate(conn, tel):
	cur = conn.cursor()
 
	cur.execute("DELETE FROM account WHERE tel='" + tel + "';")
 
	cur.execute("SELECT date, sum(amount*p.primeCost), l.tel FROM log as l, product as p WHERE type='buy' and l.productCode=p.productCode and tel='" + tel + "' group by date order by date;")
	spends = cur.fetchall()
	cur.execute("SELECT date, sum(amount*p.price), l.tel FROM log as l, product as p WHERE type='sell' and l.productCode=p.productCode and tel='" + tel + "' group by date order by date;")
	incomes = cur.fetchall()
 
	i = 0;
	j = 0;
	sum = 0;
	while True:
		if (i >= len(spends) and j >= len(incomes)):
			break
		elif (i >= len(spends)):
			while j < len(incomes):
				sum += incomes[j][1]
				cur.execute('INSERT INTO account VALUES (NULL, '
				+ str(sum) + ', "' 
				+ str(incomes[j][2]) + '", "' 
				+ str(incomes[j][0]) + '" );')
				j += 1
			break
		elif (j >= len(incomes)):
			while i < len(spends):
				sum -= spends[i][1]
				cur.execute('INSERT INTO account VALUES (NULL, '
				+ str(sum) + ', "' 
				+ str(spends[i][2]) + '", "' 
				+ str(spends[i][0]) + '" );')
				i += 1
			break

		if spends[i][0] > incomes[j][0]:
			sum += incomes[j][1]
			cur.execute('INSERT INTO account VALUES (NULL, '
				+ str(sum) + ', "' 
				+ str(incomes[j][2]) + '", "' 
				+ str(incomes[j][0]) + '" );')
			j += 1
		elif spends[i][0] < incomes[j][0]:
			sum -= spends[i][1]
			cur.execute('INSERT INTO account VALUES (NULL, '
				+ str(sum) + ', "' 
				+ str(spends[i][2]) + '", "' 
				+ str(spends[i][0]) + '" );')
			i += 1
		else:
			sum = sum + incomes[j][1] - spends[i][1]
			cur.execute('INSERT INTO account VALUES (NULL, '
				+ str(sum) + ', "' 
				+ str(spends[i][2]) + '", "' 
				+ str(spends[i][0]) + '" );')
			j += 1
			i += 1
 
 
	# i = 0
	# sum = 0;
	# for income in incomes:
	# 	money = income[1]
	# 	if spends == True and income[0] == spends[i][0]:
	# 		money -= spends[i][1]
	# 		i += 1
	# 	sum += money
	# 	cur.execute('INSERT INTO account VALUES (NULL, '
	# 			+ str(sum) + ', "' 
	# 			+ str(income[2]) + '", "' 
	# 			+ str(income[0]) + '" );')

	conn.commit()
	print("account update 성공")
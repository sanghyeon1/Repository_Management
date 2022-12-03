import pymysql
import pandas as pd

def logInsert():
	df = pd.read_csv('../account_log_all.csv')
	item_list = df[['tel', 'productCode', 'amount', 'date', 'primeCost', 'cost', 'stockAmount']]

	conn = pymysql.connect(host='127.0.0.1', user='root', db='SIMS', password='1234', charset='utf8')
	cur = conn.cursor()
	row_count, column_count = df.shape

	for i in range(0, row_count):
		if int(item_list.iloc[i]["primeCost"]) > 0:
			type = "buy"
		elif int(item_list.iloc[i]["cost"]) > 0:
			type = "sell"
		else:
			type = "disposal"
		cur.execute('INSERT INTO log VALUES (NULL, "010-6324-4435", "' 
				+ str(item_list.iloc[i]['productCode']) + '", "' 
				+ str(item_list.iloc[i]['amount']) + '", "' 
				+ str(item_list.iloc[i]['date']) + '", "'
				+ type + '", "'
				+ str(item_list.iloc[i]['stockAmount']) + '" );')

	conn.commit()
	print("log insert 성공")
	conn.close()
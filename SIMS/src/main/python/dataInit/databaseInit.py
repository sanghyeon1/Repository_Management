import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', db='SIMS', charset='utf8')

cur = conn.cursor()
createAccount = "CREATE TABLE `account` (`id` int NOT NULL AUTO_INCREMENT,`income` int NOT NULL,`tel` varchar(45) DEFAULT NULL,`date` date DEFAULT NULL,PRIMARY KEY (`id`))"
createAccountPredict = "CREATE TABLE `accountPredict` (`id` int NOT NULL AUTO_INCREMENT,`predict` int DEFAULT NULL,`tel` varchar(45) DEFAULT NULL,PRIMARY KEY (`id`))"
createMember = "CREATE TABLE `member` (`user_id` varchar(45) NOT NULL,`name` varchar(45) DEFAULT NULL,`password` varchar(45) DEFAULT NULL,`tel` varchar(45) DEFAULT NULL,PRIMARY KEY (`user_id`))"
createProduct = "CREATE TABLE `product` (`id` int NOT NULL AUTO_INCREMENT,`name` varchar(45) DEFAULT NULL,`price` int DEFAULT NULL,`productCode` varchar(45) DEFAULT NULL,`primeCost` int DEFAULT NULL,PRIMARY KEY (`id`))"
createProductSales = "CREATE TABLE `productSales` (`id` int NOT NULL AUTO_INCREMENT,`sales` int DEFAULT NULL,`name` varchar(45) DEFAULT NULL,`tel` varchar(45) DEFAULT NULL,PRIMARY KEY (`id`))"
createProductSalesPredict = "CREATE TABLE `productSalesPredict` (`id` int NOT NULL AUTO_INCREMENT,`predict` int DEFAULT NULL, `tel` varchar(45) DEFAULT NULL,PRIMARY KEY (`id`))"
createLog = "CREATE TABLE `log` (`id` int NOT NULL AUTO_INCREMENT,`tel` varchar(45) DEFAULT NULL,`productCode` varchar(45) DEFAULT NULL,`amount` int DEFAULT NULL,`date` date DEFAULT NULL,`type` varchar(45) DEFAULT NULL,`stockAmount` int DEFAULT NULL,PRIMARY KEY (`id`))"

cur.execute(createAccount)
cur.execute(createAccountPredict)
cur.execute(createMember)
cur.execute(createProduct)
cur.execute(createProductSales)
cur.execute(createProductSalesPredict)
cur.execute(createLog)

conn.close()

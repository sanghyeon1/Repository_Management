import socket, threading;
import pymysql
from income import account_day_result_check;
from product_id import product_result_check;

def binder(client_socket, addr):	
  print('Connected by', addr);	
  try:	
    while True:	
      data = client_socket.recv(4);	
      length = int.from_bytes(data, "little");	
      data = client_socket.recv(length);	
      msg = data.decode();
      if ',' in msg:
        strings = msg.split(',')
      msg = strings[0]
      tel = strings[1]
      print(msg)
      print(tel)
      print('Received from', addr, msg);
      conn = pymysql.connect(host='127.0.0.1', user='root', db='SIMS', charset='utf8')
      if msg == 'account':
        account_day_result_check.account(conn, tel);
        print('income 데이터 분석 성공');
      elif msg == 'product':
        product_result_check.product(conn, tel);
        print('product 데이터 분석 성공');	
      elif msg == 'updateSales':
        print('sales update 추가할것')
        
      msg = "echo : " + msg;	
      data = msg.encode();	
      length = len(data);	
      client_socket.sendall(length.to_bytes(4, byteorder='little'));	
      client_socket.sendall(data);
  except:	
    print("except : " , addr);	
  finally:	
    client_socket.close();	
 	
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);	
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);	
server_socket.bind(('', 9999));	
server_socket.listen();	

print("server started!!")
 	
try:	
  while True:	
    client_socket, addr = server_socket.accept();	
    th = threading.Thread(target=binder, args = (client_socket,addr));	
    th.start();	
except:	
  print("server");	
finally:	
  server_socket.close();
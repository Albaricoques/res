import socket

#при разрывах соед-я, перегрузах можем недополучать сообщ-е
#ф-я для допис-я ответа пока не получим полное сообщение
def myreceive(sock, msglen): # msglen - какой длины сообщ-е хотим получить, напр 1МБ
	msg = '' # received message
	while len(msg) < msglen: 
		chunk = sock.recv(msglen-len(msg)) #get chunk of msg no more than осталось от  желаемого размера
		#print('chunk ', chunk)
		if chunk.decode() == '': # if get nothing then raise an error and try else
			raise RuntimeError("broken")
		msg = msg + chunk.decode() # otherwise append new part to already received part of message
		#print('msg is ', msg)	
	return msg # when len msg = waited msglen

#клиент мб не готов принять все сообщ-е за раз => ф-я
def mysend(sock, msg):
	totalsent = 0
	while totalsent < len(msg):
		sent = sock.send(bytes(msg[totalsent:], 'utf-8')) # returns quantity of bytes successfully sent
		print('sent ', sent)
		if sent == 0:
			raise RuntimeError("broken")
		totalsent = totalsent + sent
		#return totalsent


HOST = '127.0.0.1'
PORT = 1234
LIMIT = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	s.bind((HOST, PORT))
	s.listen(LIMIT)
	while True:

		conn, addr = s.accept()
		#далее работает с этим клиентом, 
		#остальные клиенты ждут в очереди = LIMIT
		# клиенту LIMIT+1 сервер откажет в соединении
		
		with conn:
			print('Connected by', addr)
			while True:

				#data = conn.recv(1024)
				#print(data.decode())
				data = myreceive(conn, 10) #чтобы получить точно 10 байт и не меньше
				print(data)

				if not data: break
				
				#conn.sendall(data) # echo-сервер отправляет те же данные что получил
				
				print('Your answer is ("answer #"): ')

				#data2 = bytes(input(), 'utf-8')
				#conn.sendall(data2)
				data2 = str(input()) #чтобы отправить точно полное сообщение и не меньше
				mysend(conn, data2)

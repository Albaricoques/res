import socket

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

				data = conn.recv(1024)
				print(data.decode())

				if not data: break
				
				#conn.sendall(data) # echo-сервер отправляет те же данные что получил
				
				print('Your answer is: ')

				data2 = bytes(input(), 'utf-8')
				conn.sendall(data2)

import socket

HOST = '127.0.0.1'
PORT = 1234
print('Enter port of 127.0.0.1: ')
PORT = int(input())
LIMIT = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	s.bind((HOST, PORT))
	s.listen(LIMIT)
	#fork() #prefork, мн-во процессов-воркеров
	while True:

		conn, addr = s.accept()
		#далее работает с этим клиентом, 
		#остальные клиенты ждут в очереди = LIMIT
		# клиенту LIMIT+1 сервер откажет в соединении
		
		with conn:
			print('Connected by', addr)
			while True:

				path = conn.recv(512).decode('utf-8').rstrip('\r\n')
				if not path: break
				
				path = 'files/' + str(path)
				print(path)
				
				#file = open('/www' + str(path), 'r') #from server root -> www -> path -> file
				
				#file = open(path, 'rb') #for binary files, zB .ico
				#data = file.read()
				file = open(path, 'r') #for txt, html

				#here comes БЛОКИРУЮЩИЙ ВВОД-ВЫВОД ДАННЫХ
				#реш-ся мн-вом потоков (multithreading, см файл MANY_CLIENTS_IN_ONE_TIME), 
				#мн-вом процессов-воркеров (prefork, pool of workers), 
				#комбинир.подходом
	
				data = file.read().encode('utf-8')
				conn.sendall(data)
				file.close()
			conn.close()

				#conn.sendall(data) # echo-сервер отправляет те же данные что получил
				#print('Your answer is: ')
				#data2 = bytes(input(), 'utf-8')
				#conn.sendall(data2)

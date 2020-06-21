#это клиент, открыть в другой вкладке
import socket

print("Enter text you would like to send: ")
req = str(input())
req = bytes(req, 'utf-8')

#AF_INET - работа с Internet-сетевыми сокетами, передача по сети
#отличный от данного параметр - передача по ЛОКАЛЬНОЙ сети в пределах одной юникс машины

#.SOCK_STREAM - работа по протоколу TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	s.connect(('127.0.0.1', 1234))
	s.send(req)

	print(s)

	rsp = s.recv(1024) # получение данных +(размер буфера, сколько данных хотим получить)

	print(rsp)
	print(rsp.decode())
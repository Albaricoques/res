#это клиент, открыть в другой вкладке
import socket

#при разрывах соед-я, перегрузах можем недополучать сообщ-е
#ф-я для допис-я ответа пока не получим полное сообщение
def myreceive(sock, msglen): # msglen - какой длины сообщ-е хотим получить, напр 1МБ
	msg = '' # received message
	while len(msg) < msglen: 
		chunk = sock.recv(msglen-len(msg)) #get chunk of msg no more than осталось от  желаемого размера
		print('chunk client is ', chunk)
		if chunk.decode() == '': # if get nothing then raise an error and try else
			raise RuntimeError("broken")
		msg = msg + chunk.decode() # otherwise append new part to already received part of message
	return msg # when len msg = waited msglen

#server мб не готов принять все сообщ-е за раз => ф-я
def mysend(sock, msg):
	totalsent = 0
	while totalsent < len(msg):
		sent = sock.send(bytes(msg[totalsent:], 'utf-8')) # returns quantity of bytes successfully sent
		if sent == 0:
			raise RuntimeError("broken")
		totalsent = totalsent + sent
		print('totalsent by client ', totalsent)


req = b"Hello tcp!"

#AF_INET - работа с Internet-сетевыми сокетами, передача по сети
#отличный от данного параметр - передача по ЛОКАЛЬНОЙ сети в пределах одной юникс машины

#.SOCK_STREAM - работа по протоколу TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	s.connect(('127.0.0.1', 1234))

	while True:

		print("Enter 'question #': ")
		req = str(input())

		#req = bytes(req, 'utf-8')
		#s.send(req)
		mysend(s, req) #чтобы отправить точно полное сообщение и не меньше

		#print(s)

		#rsp = s.recv(1024) # получение данных +(размер буфера, сколько данных хотим получить)
		rsp = myreceive(s, 8) #чтобы получить точно 8 байт и не меньше

		print(rsp)
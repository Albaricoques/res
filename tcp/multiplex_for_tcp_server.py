#multiplex for making НЕБЛОКИРУЮЩЕГО ВВОДА-ВЫВОДА, EVENT-DRIVEN 
#https://stepik.org/lesson/14825/step/7?unit=4174

readsocks, writesocks = [...], [...] # сокеты
while True:
	readables, writeables, exceptions = \
		select(readsocks, writesocks, []) #select, kqueue, epoll, aio ...
	for sockobj in readables:
		data = sockobj.recv(512)
		if not data:
			sockobj.close()
			readsocks.remove(sockobj)
		else:
			print('\tgot', data, 'on', id(sockobj))
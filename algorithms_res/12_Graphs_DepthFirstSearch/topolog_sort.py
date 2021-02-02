''' H. Topological sort
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

You are given a directed graph. Find its topological sorting.

Input
The first line contains two integers n and m (1≤n≤100000,m≤100000) — the number of vertices and the number of edges in the graph, respectively.
Next m lines describe edges of the graph. Each line contains two integers v and u (1≤v,u≤n; v≠u) — describing the edge starting at v and ending at u.

Output
If no topological sorting exists, output "-1".
Otherwise, output the sequence of vertices which describes the topological ordering. 
If several orderings exist, output any.

Example
6 6
1 2
3 2
4 2
2 5
6 5
4 6
#4 6 3 1 2 5 
'''

import sys
import threading
 
threading.stack_size(43500000)
sys.setrecursionlimit(65010)

n,m = map(int,sys.stdin.readline().split())
lst = [list() for i in range(n)]
color = [1 for i in range(n)]
ans = True
for i in range(m):
	start, end = map(int, sys.stdin.readline().split())
	if end-1 in lst[start-1]:
		continue
	if start-1 in lst[end-1]:
		ans=False
		continue
	lst[start-1].append(end-1)
	color[end-1] = 0

stack = list()

class dfs_class:
	def __call__(self):
		global color
		npeaks = sum(color)
		if npeaks:
			ans = True
			peaks = list()
			for i in range(npeaks):
				ind = color.index(1)
				peaks.append(ind)
				color[ind]=0
		else:
			ans = False

		if ans:
			for peak in peaks:
				ans &= self.dfs(peak)
				if not ans:
					break
		if ans and len(stack)==n:
			stack.reverse()
			print(*stack)
		else:
			print(-1)



	def dfs(self,v):
		global color, lst, stack
		if color[v]==1:
			#значит, мы в этой ветке
			#и вернулись еа себя же, 
			#это цикл, => сортинг невозможен
			return False
		color[v] = 1
		#подсветили ветку
		if lst[v] == [-1]:
			#=> к этому узлу приходили с другой стороны, 
			#но по идее всех его детей мы должны были обработать тогда же, 
			#поэтому просто скипаем 
			color[v]=0
			return True

		for u in lst[v][::-1]:
			if not self.dfs(u):
				return False
				#если ретёрнит фолс, 
				#значит, там где то был цикл, 
				#значит, сортинг невозможен
			lst[v].pop() # после лбработки чайлда удаляем ссылку к нему
			
		lst[v] = [-1] # после обработки узла метим его как обработанный 
		
		#if v not in stack:
		#если рвньше не добавили этот узелв стак, то добавляем сейчас
		#но как мы можем прийти к такой ситуации,
		# если потом просто скипааем такие узлы? 
		# не, надо просто закоментить
		stack.append(v+1)
		color[v]=0
		# убрали подсветку узла, 
		#так что если на него придет ссылка от другого узла, 
		# это будет норм, 
		#потому что цикл не внутри одной ветки а между ветками, 
		#а это допустимо при сортинге 
		#(1-2 2-3 1-3, направленный граф, => сортинг: 1 2 3)
		
		#если сначала зашел в ветку с онли 3:
		#-добавил в стэк 3
		#-ушел в другую ветку
		#- 3 есть, => вернулся выше
		#- добавил в стек 2, вернулся выше
		#- добавил 1
		# => все правильно
		return True #ans

if m>0 and ans:
	thread = threading.Thread(target=dfs_class())
	thread.start()
	thread.join()
else:
	print(*list(range(1,n+1)))


'''
4 5
1 2
1 3
2 3
3 1
3 4
YES
1 2 3

4 4 
1 2
1 3
2 3
3 4
NO

6 6
1 2
2 3
3 4
4 5
5 6
6 4
YES
5 6 4

example2 original
? ?
5 11
11 2
11 9
11 10
7 11
7 8
8 9
3 8
3 10

adjusted
8 9
1 2
2 3
2 4
2 5
6 2
6 7
7 4
8 7
8 5

'''


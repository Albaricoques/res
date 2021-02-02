''' G. Looking for cycle
time limit per test: 2 second;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

You are given a directed graph. You have to find whether the graph contains a cycle. Output any if it does.

Input
The first line contains two integers n and m (1≤n≤10^5,m≤10^5) — the number of vertices and the number of edges in the graph, respectively. 
Next m lines describe edges of the graph. Each line contains two integers v and u (1≤v,u≤n; v≠u) — describing the edge starting at v and ending at u.

Output
If there is no cycle in the graph output "NO". 
Otherwise, output "YES" on the first line, and 
the second line should contain the sequence of vertices which describes the cycle. 
If several cycles exist, output any.

Example
3 3
1 2
2 3
3 1
#YES
#2 3 1 
'''

import sys
import threading
 
threading.stack_size(43500000)
sys.setrecursionlimit(55010)

n,m = map(int,sys.stdin.readline().split())

lst = [list() for i in range(n)]
for i in range(m):
	start, end = map(int, sys.stdin.readline().split())
	if end-1 in lst[start-1]:
		continue
	lst[start-1].append(end-1)

class dfs_class:
	def __call__(self):
		global n, color, ans
		for v in range(n):
			if not color[v]:
				ans = self.dfs_start(v)
				if ans:
					break


	def dfs(self,v, prev):
		global color, lst
		color[v] = 1
		ans = False
		for u in lst[v]:
			if not color[u]:
				ans = self.dfs(u, v)
				if ans:
					if ans[-1] != ans[0]: 
						ans.append(v+1)
						return ans
					else:
						return ans
			elif color[u]==1:
				return [u+1,v+1]#[u+1, v+1] u+1 if we had list of color-prev, to find color[u+1] = prev, color[prev+1]=prevprev and so on
		color[v] = 2
		return ans #if lst[v] is empty

	def dfs_start(self,v):
		global color, lst
		color[v] = 1
		ans = False
		for u in lst[v]:
			if not color[u]:
				ans = self.dfs(u,v)
				if ans:
					if ans[-1] != ans[0]: 
						ans.append(v+1)
						return ans
					else:
						return ans
			elif color[u]==1:
				return [u+1,v+1]#[u+1, v+1] u+1 if we had list of color-prev, to find color[u+1] = prev, color[prev+1]=prevprev and so on
		color[v] = 2
		return ans #if lst[v] is empty

color = [0 for i in range(n)]
ans = False
if m>1:
	thread = threading.Thread(target=dfs_class())
	thread.start()
	thread.join()

if ans:
	ans.pop()
	ans.reverse()
	
	print('YES')
	print(*ans)
else:
	print('NO')


'''
4 6
1 2
1 3
2 3
3 1
3 4
4 4
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
'''

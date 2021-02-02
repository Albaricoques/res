''' D. Forest
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

You are given an undirected unweighted graph. Determine if it is a tree.

Input
The first line contains a number n (1 ≤ n ≤ 100) — the number of nodes in the graph. Next n lines contain the adjacency matrix — n lines contain n numbers, either 0 or 1.

Output
Output "YES" if the graph is a tree, and "NO", otherwise.

Examples
6
0 1 1 0 0 0
1 0 1 0 0 0
1 1 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
0 0 0 0 0 0
#NO

3
0 1 0
1 0 1
0 1 0
#YES
'''

#a tree with N nodes has exactly N-1 edges. 
#Any adjacency mtx representing a tree will have exactly 2(N-1) 1's

import sys

n = int(sys.stdin.readline())
ans = True
summ = 0
s = list()

for i in range(n):
	s.append(list(map(int, sys.stdin.readline().split())))
	x = sum(s[i])
	summ += x

def p(s):
	for i in s:
		print(*i)
	print()

def no_cycles_dfs(s, v, prev, was, n):
	if was[v]:
		return s, was, False
	was[v] = True
	ans = True
	s[v][prev] = 0
	for nxt in range(n):
		if s[v][nxt]:
			s[v][nxt] = 0
			s,was,x = no_cycles_dfs(s,nxt, v, was, n)
			ans = ans & x
	return s, was,ans

def no_cycles_dfs_start(s, v, n, was=None):
	was = [False for i in range(n)]
	was[v] = True
	ans = True
	for nxt in range(n):
		if s[v][nxt]:
			s[v][nxt] = 0
			s,was,x = no_cycles_dfs(s,nxt, v, was, n)
			ans = ans & x
	return ans, was

if ans:
	if summ != 2*(n-1):
		ans = False
	else:
		ans, was = no_cycles_dfs_start(s,0, n)

if ans :
	print('YES')
else:
	print('NO')

'''
4
0 0 0 1
0 0 0 1
0 0 0 1
1 1 1 0


2
0 1
1 0

4
0 1 1 1
1 0 0 0
1 0 0 0
1 0 0 0

3
0 1 0
0 0 1
1 0 0

4
0 1 0 1
1 0 0 1
0 0 0 1
1 1 1 0
cycled

4
0 1 1 0
1 0 0 1
1 0 0 1
0 1 1 0

'''

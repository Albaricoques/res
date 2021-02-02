''' B. Check undirected graph
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

You are given a matrix n × n which consists of zeroes and ones. Determine if this matrix could be the adjacency matrix of a simple undirected graph.

Input
The first line contains one integer n (1 ≤ n ≤ 100) — the number of vertices in the graph. Next n lines contain the matrix — n lines by n integers, each is either 0 or 1.

Output
Output YES, if given matrix could be an adjacency matrix of a simple undirected graph, and NO, otherwise.

Examples
3
0 1 1
1 0 1
1 1 0
#YES

3
0 1 0
1 0 1
1 1 0
#NO

3
0 1 0
1 1 1
0 1 0
#NO
'''

import sys

n = int(sys.stdin.readline())
ans = True
s = list()
for i in range(n):
	s.append(list(map(int, sys.stdin.readline().split())))
	if s[i][i]==1:
		ans = False

if ans:
	for i in range(n):
		for j in range(n):
			if s[i][j]!=s[j][i]:
				ans = False

if ans:
	print('YES')
else:
	print('NO')

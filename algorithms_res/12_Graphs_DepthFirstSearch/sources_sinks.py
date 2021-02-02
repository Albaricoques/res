''' C. Sources and sinks
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

A node of a directed graph is called source if it does not have any incoming edges. 
And node is called sink if it does not have any outcoming edges.
A directed graph is given by its adjacency matrix. 
Output all the source-nodes and all the sink-nodes.

Input
The first line contains one number n (1 ≤ n ≤ 100) — number of nodes in graph. 
Next n lines contains the adjacency matrix — n lines contain n numbers, either 0 or 1.

Output
The first line of the output should contain the number of sources in the graph followed by the indices of source-nodes in the increasing order. 
The second line of the output should contain sink-nodes in the same format.

Example
5
0 0 0 0 0
0 0 0 0 1
1 1 0 0 0
0 0 0 0 0
0 0 0 0 0
# 2 3 4 
# 3 1 4 5 
'''

import sys

n = int(sys.stdin.readline())
ans = True
s = list()
sinks = list()
notsources = list()

for i in range(n):
	s.append(list(map(int, sys.stdin.readline().split())))
	if sum(s[i])==0:
		sinks.append(i+1)
	else:
		for j in range(n):
			if s[i][j]==1 and j not in notsources:
				notsources.append(j)

srcs = list()
for i in range(n):
	if i not in notsources:
		srcs.append(i+1)

print(len(srcs), *srcs)
print(len(sinks),*sinks)

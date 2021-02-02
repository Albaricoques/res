''' A. Calculating number of edges of undirected graph
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

A simple undirected graph is given by its adjacency matrix. Find the number of edges in this graph.

Input
The first line contains a single number N (1 ≤ N ≤ 100) — the number of nodes in graph. Next lines contain the adjacency matrix — N lines contain N numbers, either 0 or 1.

Output
Output the number of edges in the given graph.

Example
3
0 1 1
1 0 1
1 1 0
#3
'''

import sys

n = int(sys.stdin.readline())
edges = 0
for i in range(n):
	s = list(map(int, sys.stdin.readline().split()))
	edges += sum(s[i:])

print(edges)

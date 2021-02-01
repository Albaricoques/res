'''
C. Python Program for Floyd Warshall Algorithm 
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

You are given a fully-connected directed weighted graph. Please find the shortest path between each pair of nodes.
Input

The first line of the input contains one integer n
(1≤n≤100) — the number of vertices. Next n lines contain n integers each and represent an adjacency matrix with weights. All integers do no exceed 100

in absolute value. The main diagonal contains only zeros.
Output

Output n
lines with n integers each — the matrix of the distance between each pair of nodes, i.e., j-th number in i-th line represents the weight of the shortest path from vertex i to vertex j

.
Example
Input
Copy

4
0 5 9 100
100 0 2 8
100 100 0 7
4 100 100 0

Output
Copy

0 5 7 13 
12 0 2 8 
11 16 0 7 
4 9 11 0 

'''

INF = 10001

def floydWarshall(graph): 

	dist = list(map(lambda i : list(map(lambda j : j , i)) , graph)) 

	for k in range(n): 
		for i in range(n): 
			for j in range(n): 
				dist[i][j] = min(dist[i][j] , 
								dist[i][k]+ dist[k][j] 
								) 
	printSolution(dist) 

def printSolution(dist): 
	for i in range(n): 
		for j in range(n): 
			if(dist[i][j] > 100): 
				print(-1, end=' ')
			else: 
				print(dist[i][j], end = ' ')
			if j == n-1: 
				print("")

import sys
n = int(sys.stdin.readline())
graph = list()
for i in range(n):
	graph.append(list(map(int,sys.stdin.readline().split())))
floydWarshall(graph); 

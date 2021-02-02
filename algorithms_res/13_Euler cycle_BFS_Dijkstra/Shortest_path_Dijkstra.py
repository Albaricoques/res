# Dijkstra's single source shortest path algorithm. 
#The program is for adjacency matrix representation of the graph 

''' C. Shortest path
time limit per test: 1 second;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

You are given a directed weighted graph without negative edges. 
Find the shortest distance from one vertex to another one.

Input
The first line of the input contains three integers n, s and f (1 ≤ n ≤ 2000, 1 ≤ s, f ≤ n) 
— the number of vertices, the start vertex and the end vertex. 
Next n lines contain n integers each — the adjacency matrix of the graph, where  
- 1 means non-existence of an edge. 
The weight of each edge does not exceed 10^9. 
The main diagonal contains only zeros.

Output
The sole line of the output should contain the distance from the start vertex to the end vertex, 
or  - 1 if there is no path between them.

Example
3 1 2
0 -1 2
3 0 -1
-1 4 0
#6
'''

import sys 

class Graph(): 

	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = list()

	def printSolution(self, dist, end): 
		if dist[end]>1000:
			print(-1, end=' ' )
		else:
			print(dist[end])

	def minDistance(self, dist, sptSet): 
		min = sys.maxsize
		min_index=-1
		for v in range(self.V): 
			if dist[v] < min and sptSet[v] == False: 
				min = dist[v] 
				min_index = v 
		return min_index

	def dijkstra(self, src, end): 
		dist = [sys.maxsize] * self.V 
		dist[src] = 0
		sptSet = [False] * self.V 

		for cout in range(self.V): 
			u = self.minDistance(dist, sptSet) 
			sptSet[u] = True
			for v in range(self.V): 
				if self.graph[u][v] > -1 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
						dist[v] = dist[u] + self.graph[u][v] 

		self.printSolution(dist,end) 

n,s,f = map(int,sys.stdin.readline().split())
g = Graph(n) 

for i in range(n):
	g.graph.append(list(map(int,sys.stdin.readline().split())))

g.dijkstra(s-1, f-1); 

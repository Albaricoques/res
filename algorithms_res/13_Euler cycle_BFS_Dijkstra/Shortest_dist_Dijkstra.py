# Dijkstra's single source shortest path algorithm. 
#The program is for adjacency matrix representation of the graph 

''' B. Shortest distances
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

Given a directed graph. Find the distances from the vertex x to all other vertices of the graph.

Input
The first line of the input file contains two integers n and x (1≤n≤1000, 1≤x≤n) 
— the number of vertices in the graph and the start vertex, respectively. 
Next n lines contain n numbers each, the adjacency matrix of the graph: 
in the i-th row the j-th number is "1" if the vertices i and j are connected by an edge, 
and "0" if there is no edge between them. 
On the main diagonal of the matrix all numbers are zeros.

Output
Output numbers d1,d2,…dn, where di is −1, if there is no path from x to i 
and the minimum distance between x and i, otherwise.

Example
6 5
0 1 1 0 0 0
1 0 0 0 0 0
1 1 0 0 0 0
0 0 0 0 1 0
0 0 1 1 0 0
0 1 0 0 0 0
#2 2 1 1 0 -1
'''

import sys 

class Graph(): 

	def __init__(self, vertices): 

		self.V = vertices 
		self.graph = list() 

	def printSolution(self, dist): 

		for node in range(self.V): 
			if dist[node]>1000:
				print(-1, end=' ' )
			else:
				print(dist[node], end=' ' )
		print()

	def minDistance(self, dist, sptSet): 

		minn = sys.maxsize
		min_index=-1
		for v in range(self.V): 
			if dist[v] < minn and sptSet[v] == False: 
				minn = dist[v] 
				min_index = v 

		return min_index

	def dijkstra(self, src): 

		dist = [sys.maxsize] * self.V 
		dist[src] = 0
		sptSet = [False] * self.V 

		for cout in range(self.V): 
			u = self.minDistance(dist, sptSet) 
			sptSet[u] = True
			for v in range(self.V): 
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
						dist[v] = dist[u] + self.graph[u][v] 

		self.printSolution(dist) 

n,x = map(int,sys.stdin.readline().split())
g = Graph(n) 

for i in range(n):
	g.graph.append(list(map(int,sys.stdin.readline().split())))

g.dijkstra(x-1); 

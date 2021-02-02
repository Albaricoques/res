# Dijkstra's single source shortest path algorithm. 
#The program is for adjacency list representation of the graph 

''' D. Shortest path 2
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

You are given an undirected connected weighted graph. 
Find the shortest distance from the first vertex to all others.

Input
The first line of the input contains two integers n and m (2≤n≤30000,1≤m≤400000) 
— the number of vertices and the number of edges, correspondingly.

Next m lines contain the description of edges. 
Each edge is represented with three integers: the identifiers of its ends and the weight. 
The weight of each edge is a non-negative integer that does not exceed 10^4.

Output
The sole line of the output should contain n integers 
— the distances from the first vertex to all others in the order of their identifiers.

Example
4 5
1 2 1
1 3 5
2 4 8
3 4 1
2 3 3
#0 1 4 5 
'''

from collections import defaultdict
import sys

class Heap():

	def __init__(self):
		self.array = []
		self.size = 0
		self.pos = []

	def newMinHeapNode(self, v, dist):
		minHeapNode = [v, dist]
		return minHeapNode

	def swapMinHeapNode(self,a, b):
		t = self.array[a]
		self.array[a] = self.array[b]
		self.array[b] = t

	def minHeapify(self, idx):
		smallest = idx
		left = 2*idx + 1
		right = 2*idx + 2

		if left < self.size and self.array[left][1] < self.array[smallest][1]:
			smallest = left

		if right < self.size and self.array[right][1] < self.array[smallest][1]:
			smallest = right

		if smallest != idx:
			self.pos[ self.array[smallest][0]] = idx
			self.pos[ self.array[idx][0]] = smallest
			self.swapMinHeapNode(smallest, idx)
			self.minHeapify(smallest)

	def extractMin(self):
		if self.isEmpty() == True:
			return
		root = self.array[0]
		lastNode = self.array[self.size - 1]
		self.array[0] = lastNode
		self.pos[lastNode[0]] = 0
		self.pos[root[0]] = self.size - 1
		self.size -= 1
		self.minHeapify(0)
		return root

	def isEmpty(self):
		return True if self.size == 0 else False

	def decreaseKey(self, v, dist):
		i = self.pos[v]
		self.array[i][1] = dist
		while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:
			self.pos[ self.array[i][0] ] = (i-1)//2
			self.pos[ self.array[(i-1)//2][0] ] = i
			self.swapMinHeapNode(i, (i - 1)//2 )
			i = (i - 1) // 2;

	def isInMinHeap(self, v):
		if self.pos[v] < self.size:
			return True
		return False


def printArr(dist, n):
	for i in range(n):
		print(dist[i], end=' ')
	print()


class Graph():
	def __init__(self, V):
		self.V = V
		self.graph = defaultdict(list)

	def addEdge(self, src, dest, weight):
		newNode = [dest, weight]
		self.graph[src].insert(0, newNode)
		newNode = [src, weight]
		self.graph[dest].insert(0, newNode)

	def dijkstra(self, src):
		V = self.V
		dist = [] 
		minHeap = Heap()
		for v in range(V):
			dist.append(sys.maxsize)
			minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]))
			minHeap.pos.append(v)
		minHeap.pos[src] = src
		dist[src] = 0
		minHeap.decreaseKey(src, dist[src])
		minHeap.size = V;
		while minHeap.isEmpty() == False:
			newHeapNode = minHeap.extractMin()
			u = newHeapNode[0]
			for pCrawl in self.graph[u]:

				v = pCrawl[0]
				if minHeap.isInMinHeap(v) and dist[u] != sys.maxsize and  pCrawl[1] + dist[u] < dist[v]:
						dist[v] = pCrawl[1] + dist[u]
						minHeap.decreaseKey(v, dist[v])

		printArr(dist,V)


n,m = map(int,sys.stdin.readline().split())
graph = Graph(n) 

for i in range(m):
	start, end, cost = map(int,sys.stdin.readline().split())
	graph.addEdge(start-1, end-1, cost)

graph.dijkstra(0); 

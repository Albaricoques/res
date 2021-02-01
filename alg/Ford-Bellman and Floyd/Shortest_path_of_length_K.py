'''
A. The shortest path of length K
time limit per test
4 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

You are given a directed graph. Please, find the shortest paths from S to all other vertices that consist of exactly K edges.
Input

The first line of the input contains four integers n, m, K and S (1 ≤ n ≤ 104, 0 ≤ m ≤ 104, 0 ≤ K ≤ 100, 1 ≤ S ≤ n) — the number of vertices, the number of edges, the total number of edges on paths, and the start vertex.

Next m lines contain the description of edges. Each edge is represented with three integers ai, bi, w (1 ≤ ai, bi ≤ n,  - 105 ≤ w ≤ 105) — the ends of the edge and its weight.
Output

The output should contain n integers on a separated line. i-th integer should represent the length of the minimal path between S and t with exactly K edges, or  - 1 if there is no such path.
Examples
Input
Copy

3 3 1 1
1 2 100
2 3 300
1 3 2

Output
Copy

-1
100
2

Input
Copy

3 3 2 1
1 2 100
2 3 300
1 3 2

Output
Copy

-1
-1
400
'''

import sys

class Edge :

    def __init__(self, src, dst, weight) :
         self.src = src 
         self.dst = dst 
         self.weight = weight
    def __str__(self):
    	return ' '.join(map(str,[self.src,self.dst,self.weight]))

class Graph :

    def __init__(self, edge_list, node_cnt) :
         self.edge_list = edge_list
         self.node_cnt  = node_cnt

    def BellmanFordShortestPath(self, src):#, n_edges) :

        # Initialize the distance from the source node S to all other nodes as infinite (999999999) and to itself as 0.
        distance = [999999999999] * self.node_cnt
        distance[src] = 0

        for node in range(self.node_cnt) :
            print('node', node)
            for edge in self.edge_list :
                print('edge', edge)
                print('distance[edge.dst]',distance[edge.dst])
                print('distance[edge.src]',distance[edge.src])
                print('distance[edge.src] + edge.weight',distance[edge.src] + edge.weight)
                if (distance[edge.dst] > distance[edge.src] + edge.weight) :
                    distance[edge.dst] = distance[edge.src] + edge.weight
                    print('distance[edge.dst] > distance[edge.src] + edge.weight')
        for edge in self.edge_list :

            if (distance[edge.dst] > distance[edge.src] + edge.weight) :
                print("Negative weight cycle exist in the graph")
                print(edge.src, edge.dst)
                print(-1)

        for node in range(self.node_cnt) : 
            print("Source Node("+str(src)+") -> Destination Node("+str(node)+") : "+str(distance[node]))

def main() :

	n,m, S = map(int,sys.stdin.readline().split())
    #K, 
	lst = list()
	for i in range(m):
		v,u,m = map(int,sys.stdin.readline().split())
		lst.append(Edge(v-1,u-1,m))

	g=Graph(lst, n)
	g.BellmanFordShortestPath(S-1)


main()

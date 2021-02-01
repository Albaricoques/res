'''
B. Shortest paths
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

You a given a weighted directed graph and vertex s. You should find the shortest distance from s to all the other vertices.
Input

The first line of the input contains three integers n, m, s (2 ≤ n ≤ 2 000, 1 ≤ m ≤ 5 000) — the number of vertices, the number of edges, and the identifier of the start vertex.

Next m lines contain the description of edges. Each edge is represented with three integers — the ends and the weight. The weight of a graph is an integer and does not exceed 1015 by the absolute value. The graph can contain loops and multiple edges between a pair of vertices.
Output

The output should contain n lines — for each vertex, output the length of the shortest path from s. If there is no path then output "*", and if there does not exist a shortest path then output "-".
Example
Input
Copy

6 7 1
1 2 10
2 3 5
1 3 100
3 5 7
5 4 10
4 3 -18
6 1 -1

Output
Copy

0
10
-
-
-
*
'''

import sys

inf = 10**24 # 10**5**2 + 1#100000000

n,m, S = map(int,sys.stdin.readline().split())
S -=1
g = [dict() for i in range(n)]
for i in range(m):
    a,b,w = map(int,sys.stdin.readline().split())
    if not (b-1 in g[a-1] and g[a-1][b-1]<=w):
        g[a-1][b-1] = w


d = [inf for i in range(n)]
d[S] = 0
negative = list()

for i in range(n):
    for v in range(n):
        for u in g[v]:
            #print(v, u, 'k', k)
            #print(d[k+1][u], d[k][v], g[v][u])
            if d[u]>d[v]+g[v][u]:
                d[u] = d[v]+g[v][u]

for v in range(n):
    for u in g[v]:
        if d[u]>d[v]+g[v][u]:
            d[u] = d[v]+g[v][u]
            #print('negative loop', v, u)
            negative.append(v)
#print(negative)

allnegative=list()

def dfs(v):
    #print(v)
    if v in allnegative:
        return
    if abs(d[v])<10**20:
        allnegative.append(v)
        for i in g[v]:
            if i not in allnegative:
                dfs(i)
        #print(allnegative)

for i in negative:
    dfs(i)
#print(allnegative)


for node in range(n) : 
    #print(distance[node],distance2[node])
    if abs(d[node])>10**20:
        print('*')
    elif node in allnegative:
        #print("Source Node("+str(src)+") -> Destination Node("+str(node)+") : "+'-')
        print('-')
    else: #if distance[node]<10**16:
        #print("Source Node("+str(src)+") -> Destination Node("+str(node)+") : "+str(distance[node]))
        print(d[node])
        #print(node+1)
        #print(d[node],d2[node])

''' A. The shortest path of length K
time limit per test: 4 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

You are given a directed graph. 
Please, find the shortest paths from S to all other vertices that consist of exactly K edges.

Input
The first line of the input contains four integers n, m, K and S 
(1 ≤ n ≤ 10^4, 0 ≤ m ≤ 10^4, 0 ≤ K ≤ 100, 1 ≤ S ≤ n) 
— the number of vertices, the number of edges, the total number of edges on paths, and the start vertex.

Next m lines contain the description of edges. 
Each edge is represented with three integers ai, bi, w(1≤ai,bi≤n,-10^5≤w≤10^5) 
— the ends of the edge and its weight.

Output
The output should contain n integers on a separated line. 
i-th integer should represent the length of the minimal path between S and t with exactly K edges, 
or  - 1 if there is no such path.

Examples
3 3 1 1
1 2 100
2 3 300
1 3 2
#-1
#100
#2

3 3 2 1
1 2 100
2 3 300
1 3 2
#-1
#-1
#400
'''
import sys
 
inf = 10**5**2 + 1#100000000
 
n,m, K, S = map(int,sys.stdin.readline().split()) #K is number of edges on path , S is start node
S -=1
g = [dict() for i in range(n)]
for i in range(m):
    a,b,w = map(int,sys.stdin.readline().split())
    if not (b-1 in g[a-1] and g[a-1][b-1]<=w):
        g[a-1][b-1] = w
 
 
d = [[inf for i in range(n)] for j in range(K+1)]
d[0][S] = 0
 
k=0
v = S
new_v = S
while k<K:
    for v in range(n):
        for u in g[v]:
            if d[k+1][u]>d[k][v]+g[v][u]:
                d[k+1][u] = d[k][v]+g[v][u]
    k+=1
 
i=d[K]
for j in i:
    print(j) if j<=10**7 else print(-1) 

''' E. Connected components
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

Your task is to find connected components of a given undirected graph.

Input
The first line of the input file contains two integers n and m (1≤n≤100000, 0≤m≤200000) 
— the number of vertices and edges of the graph.
The following m lines contain the descriptions of edges one per line. 
Edge number i is described by two integers bi, ei (1≤bi,ei≤n) — the numbers of its ends. 
Loops and parallel edges are allowed.

Output
In the first line of the output file output an integer k, the number of connected components in the graph.
In the second line output n numbers a1,a2,…,an from 1 to k, 
where ai is the identifier of the connected component the i-th vertex belongs to.

Examples
3 1
1 2
#2
#1 1 2

4 2
1 3
2 4
#2
#1 2 1 2
'''

import sys
import threading
 
threading.stack_size(21000000)
sys.setrecursionlimit(57500)
 
ans = 0
num = []
 
class dfs_class:
    def __call__(self):
        global n, used, ans
        for i in range(n):
            if used[i]:
                continue
            ans += 1
            self.dfs(i)
 
    def dfs(self, v):
        global g, used, num
        num[v] = ans
        used[v] = True
        for to in g[v]:
            if used[to]:
                continue
            self.dfs(to)
 
 
n, m = map(int, input().split())
g = [[] for i in range(n)]
used = [False] * n
num = [0] * n
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
 
thread = threading.Thread(target=dfs_class())
 
thread.start()
thread.join()
 
print(ans)
for i in range(n):
    print(num[i], end=' ')

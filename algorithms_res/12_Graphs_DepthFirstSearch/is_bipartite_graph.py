''' F. Bipartite graph
time limit per test: 1 second;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

The bipartite graph is an undirected graph whose vertices can be divided 
into two disjoint sets L and R, such that 
for every edge (u,v), either (u->L, v->R) or (u->R, v->L).

You are given an undirected graph. Check if this graph is bipartite.

Input
The first line contains two integers n and m (1 ≤ n ≤ 100 000; 0 ≤ m ≤ 200 000) 
— number of vertices and edges in the graph, respectively.
Next m lines contain the description of edges; 
i-th of these lines contains two integers ui and vi (1 ≤ ui, vi ≤ n) 
— the vertices connected by i-th edge.

Output
Output "YES", if the given graph is bipartite, or "NO", otherwise.
If the graph is bipartite output the proper division into two sets: 
for each vertex output 1, if this vertex in set L, otherwise output 2.

Examples
4 4
1 2
1 3
2 4
4 2
#YES
#1 2 2 1

3 3
1 2
2 3
3 1
#NO
'''

import sys
import threading
 
threading.stack_size(18900000)
sys.setrecursionlimit(50000)
 
ans = True
class dfs_class:
    def __call__(self):
        global n, used, ans
        for i in range(n):
            if used[i]:
                continue
            ans = self.dfs(i, -1)
            if not ans:
                return
 
    def dfs(self, v, c):
        global g, used
        ans = True
        used[v] = -c #True # if -= then if was: 1-= 1 => 0 wasn't here
        for to in g[v]:
            if used[to]==0-used[v]:
                continue
            elif used[to]==used[v]:
                return False
            ans &= self.dfs(to, used[v])
        return ans

n, m = map(int, input().split())
g = [[] for i in range(n)]
used = [0] * n
edges=0
for i in range(m):
    u, v = map(int, input().split())
    if u==v:
        ans = False
        continue
    u -= 1
    v -= 1
    if v in g[u]:
        continue
    g[u].append(v)
    g[v].append(u)
    edges+=1

if edges>= (n**2)/4: #Max edges in bipartite graph with n vertices
    ans=False

if ans:
    thread = threading.Thread(target=dfs_class())
 
    thread.start()
    thread.join()
 
if ans:
    print('YES')
    for i in used:
        if i==-1:
            print(2, end=' ')
        else:
            print(1, end=' ')
    print()
else:
    print('NO')

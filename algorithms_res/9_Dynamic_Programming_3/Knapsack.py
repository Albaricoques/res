''' D. Knapsack
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

You are given n objects. i-th object has weight mi and value ci.
You try to put them in a knapsack that can withstand the weight of not more than M. 
Find a set of objects that can be carried in a knapsack with the highest total value.

Input
The first line contains two integers n and M (1≤n,M≤1000) — the number of objects and the maximal capacity of the knapsack.
The second line contains n integers mi (1≤mi≤100) — the weights of the objects.
The third line contains n integers ci not exceeding (1≤ci≤100) — the values of the objects.

Output
The first line of the output should contain the number of items that one needs to take. 
The second line should contain the identifiers of objects (the number from 1 to n), 
which should be included in the knapsack to get the highest total value.

Example
Input
4 6
2 4 1 2
7 2 5 1

Output
3
1 3 4
'''

import sys

n, M = map(int, sys.stdin.readline().split())
wt = list(map(int, sys.stdin.readline().split()))
val = list(map(int, sys.stdin.readline().split()))

def knapSack(W, wt, val, n): 
	K = [[0 for x in range(W + 1)] for x in range(2)]
	lst = [[list() for x in range(W + 1)] for x in range(2)]
	# Build table K[][] in bottom up manner 
	for i in range(n + 1): 
		for w in range(W + 1): 
			if i == 0 or w == 0: 
				continue
			elif wt[i-1] <= w: 
				x1 = val[i-1] + K[0][w-wt[i-1]] #cost of this bar+ sum received for previous bar with capacity lower at weight of previous bar
				x2 = K[0][w] # sum received for previous bar with current capacity
				if x1>x2:
					lst[1][w] = lst[0][w-wt[i-1]].copy()
					lst[1][w].append(i)
				else:
					lst[1][w] = lst[0][w].copy()
				K[1][w] = max(x1,x2) 
			else: 
				K[1][w] = K[0][w] 
				lst[1][w] = lst[0][w].copy()
		lst[0] = lst[1].copy()
		K[0] = K[1].copy()
	return K, lst

m, lst = knapSack(M, wt, val, n)
print(len(lst[-1][-1]))
print(*lst[-1][-1])

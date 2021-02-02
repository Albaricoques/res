''' C. Knapsack without cost
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

Please, find the maximal weight of the gold that we can fit into the knapsack 
with the maximal capacity S if there are n gold bars with given weights.

Input
The first line of the input contains two integers S and n (1 ≤ n ≤ 300, 1 ≤ S ≤ 1000) — the maximal capacity of the knapsack .
The next line contains n non-negative integers that do not exceed 100 000 — the weights of the bars.

Output
The sole line of the output should contain the answer to the problem.
Examples

Input
10 3
1 4 8
Output
9

Input
20 4
5 7 12 18
Output
19
'''

import sys

S, n = map(int, sys.stdin.readline().split())

wt = list(map(int, sys.stdin.readline().split()))

def knapSack(W, wt, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(wt[i-1] 
                          + K[i-1][w-wt[i-1]],   
                              K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  

print(knapSack(S, wt, n)) 

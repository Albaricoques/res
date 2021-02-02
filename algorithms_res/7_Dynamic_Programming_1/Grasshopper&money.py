import sys


n, k = map(int, sys.stdin.readline().split()) #(1 ≤ n ≤ 30, 1 ≤ k ≤ 10)
# how many ways from 1 to n? k - max jump

C = [0, 0] + list(map(int, sys.stdin.readline().split())) + [0]

fromm = {1:0}

if n==2:
	print(0) # or C[0] when we have money on the first cell also
	print(1)
	print(1)
else:
	ans = {1:0}
	for i in range(2,n+1):
		ans[i] = -10001
		for j in range(max(1,i-k), i):
			if ans[i] < ans[j] + C[i]:
				ans[i] = ans[j]+C[i]
				fromm[i] = j
	print(ans[i])

	ans = list()
	x = i
	while x != 0:
		ans.append(x)
		x = fromm[x]
	ans.reverse()
	print(len(ans)-1)
	print(*ans)


''' E. Grasshopper and Money
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

The grasshopper is traveling from cell 1 to cell n. 
At the beginning, the grasshopper sits on cell 1. 
He can move from 1 to k cells forward in one jump.

In each cell grasshopper can get or lose several gold coins 
(for each cell this number is known). 
Determine how the grasshopper needs to jump to maximize 
the total number of coins in the end. 
Consider that the grasshopper cannot jump backwards.


Input
The first line contains two integers n and k (2 ≤ n, k ≤ 10 000) — 
the number of cells and the largest jump. 
The second line contains (n - 2) integers, 
the number of coins that the grasshopper gets on each cell, 
from the second to the n - 1-th. 
If this number is negative, the grasshopper loses coins. 
All the numbers do not exceed 10 000 by absolute value.

Output
In the first line output the maximal number of coins. 
In the second line output the number of jumps. 
In the third line output the cells visited by the grasshoper.

Example
Input
5 3
2 -3 5
Output
7
3
1 2 4 5 
'''
import sys

n, k = map(int, sys.stdin.readline().split()) #(1 ≤ n ≤ 30, 1 ≤ k ≤ 10)
# how many ways from 1 to n? k - max jump

if n == 1:
	print(1)
elif n == 2:
	print(1)
else:
	ans = {1:1,2:1}
	for i in range(3,n+1):
		for j in range(max(1,i-k), i):
			if i not in ans:
				ans[i] = 0
			ans[i] += ans[j]
	print(ans[i])


''' D. Grasshopper
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

The grasshopper is traveling from cell 1 to cell n. 
In the beginning, the grasshopper sits on cell 1. 
He can move from 1 to k cells forward in one jump. 
Please, calculate how many different ways there exists 
to travel from cell 1 to cell n.

Input
The sole line of the input contains two integers n and k 
(1 ≤ n ≤ 30, 1 ≤ k ≤ 10) — 
the number of cells and the length of the maximal jump.

Output
The sole line of the output should contain one integer — 
the answer to the problem.

Example
Input
8 2
Output
21
'''
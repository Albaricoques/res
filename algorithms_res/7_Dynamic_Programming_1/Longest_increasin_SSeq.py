'''
G. Longest increasing subsequence
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

You are given the sequence of integers, find its longest increasing subsequence.

Input
The first line of the input contains one integer n (1≤n≤1000) — the length of the sequence.
The second line contains the sequence of integers, not exceeding 10^9 by an absolute value.

Output
The first line of the output should contain one integer — the length of the longest increasing subsequence. 
The second line should contain the largest increasing subsequence of the sequence. 
If there are several answers — output any.

Example
Input
6
3 29 5 5 28 6

Output
3
3 5 28 
'''

import sys

n = int(sys.stdin.readline())

s = list(map(int, sys.stdin.readline().split()))

fromm = dict()
ans = {0:1}
ind = int()
for i in range(1,n): 
	ans[i] = 1
	for j in range(0, i): 
		if s[j] < s[i]:
			if ans[i] < ans[j]+1:
				ans[i] = ans[j]+1
				fromm[i] = j
				if ans[ind]< ans[i]:
					ind = i
print(ans[ind])

res = [s[ind]]
for x in range(ans[ind]-1):
	ind = fromm[ind]
	res.append(s[ind])
res.reverse()
print(*res)

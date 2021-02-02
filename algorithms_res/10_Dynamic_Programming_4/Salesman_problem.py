''' A. The Salesman Problem
time limit per test: 1 second;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

The Salesman (The Cat Aquariums Salesman) is going to visit n cities, visiting each city exactly once.
Help him to find the shortest possible path.

Input
The first line of the input contains one integer n(1⩽n⩽13) — the number of cities. 
Each of the next n lines contains n integers: the lengths of paths between cities.
The j-th integer in the i-th line is a(i,j) (0⩽a(i,j)⩽10^6; a(i,j)=a(j,i); a(i,i)=0) — the distance between cities i and j.

Output
The first line of the output should contain one integer — the smallest total distance that Salesman needs to travel. 
The second line should contain n integers — the order in which he should visit the cities.

Examples
Input
5
0 183 163 173 181
183 0 165 172 171
163 165 0 189 302
173 172 189 0 167
181 171 302 167 0

Output
666
4 5 2 3 1 
'''

import sys

n = int(sys.stdin.readline())

if n>1:
	a = list()

	for case in range(n):
		a.append(list(map(int, sys.stdin.readline().split())))

	dp = [[10**7 for i in range(n+1)] for j in range(2 ** n)]
	dpp = [[0 for i in range(n+1)] for j in range(2 ** n)]

	links = dict()
	for i in range(n):
		links[i+1] = 0b1<<i

	masks = range(2**n)
	for mask in sorted(masks, key=lambda x: bin(x).count('1')):
		if bin(mask).count('1') < 2:
			dp[mask] = [0 for i in range(n+1)]
			continue

		for end in range(n+1):
			if end==0:
				dp[mask][end] = 0
				continue
			if not mask&links[end]:
				continue

			for nxt in range(1,n+1):
				if mask&links[nxt] and end!=nxt:
					x = dp[mask^links[end]][nxt]+a[nxt-1][end-1]
					if dp[mask][end] > x:
						dp[mask][end] = dp[mask^links[end]][nxt]+a[nxt-1][end-1] 
						dpp[mask][end] = nxt

	mask = 2**n-1
	ans = min(dp[mask][1:])
	ind = dp[mask].index(ans)
	print(ans)
	print(ind, end = ' ') #1
	for i in range(n-1):
		ind2 = dpp[mask][ind] #3
		mask -= links[ind]
		ind = ind2 #3
		print(ind, end = ' ')
	print()
else:
	sys.stdin.readline()
	print(0)
	print(1)

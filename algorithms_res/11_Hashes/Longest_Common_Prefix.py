''' C. Longest Common Prefix
time limit per test: 10 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

You are given string s of length n and m pairs of indices. 
For each pair of indices ai,bi 
find the length of the longest common prefix of strings s[ai..n−1] and s[bi..n−1].

Input
The first line of the string contains s(the length of s is in [1,10^5], and s consists of only Latin letters).
The second line contains integer m (1≤m≤10^5). 
Next m lines contain two integers each, ai,bi (0≤ai,bi≤n−1, where n is the length of s).

Output
For each query output one integer per line — the length of the longest common prefix of s[ai..n−1] и s[bi..n−1].

Example
Input
abacaba
21
0 1
0 2
0 3
0 4
0 5
0 6
1 2
1 3
1 4
1 5
1 6
2 3
2 4
2 5
2 6
3 4
3 5
3 6
4 5
4 6
5 6

Output
0
1
0
3
0
1
0
0
0
2
0
0
1
0
1
0
0
0
0
1
0
'''

import sys

s = list(map(ord, sys.stdin.readline()))
m = int(sys.stdin.readline())

length = len(s)

for step in range(m):
	a,b = map(int,sys.stdin.readline().split())
	if a==b:
		print(length-a-1)
		continue
		
	ans = 0
	a,b = sorted([a,b])
	while b < length:
		if s[a]==s[b]:
			ans+=1
		else:
			break
		a += 1
		b += 1
	print(ans)

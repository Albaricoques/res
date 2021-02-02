''' B. Hashes of Substrings
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

Polynomial hash of string s of length n is h(s)=(∑(i=0)(n−1) s[i]*t^(n−i−1))*mod(r).
Here, s[i] is the ASCII-code of i-th symbol of string s using 0-indexing. 

For example, for string "abacaba" the hash is calculated as follows: 
(97*t^6+98*t^5+97*t^4+99*t^3+97*t^2+98*t+97)*mod(r).

You are given integers t and r, string s and m pairs of indices. 
For each pair of indices ai,bi find the hash of s[ai..bi].

Input
The first line of the input contains two integers t and r (1≤t≤10^9, 2≤r≤10^9).
The second line of the input contains s (the length of the string is in [1,10^5], and s consists of Latin letters).
The third line contains m(1≤m≤10^5). 
Next m lines contain two integers each, ai,bi (0≤ai≤bi≤n−1, where n is the length of s).

Output
For each query output one integer per line — the hash of s[ai..bi].

Example
Input
7 19
abacaba
18
0 0
0 1
0 2
0 3
0 4
0 5
0 6
1 1
1 2
1 3
1 4
1 5
1 6
2 2
2 3
2 4
2 5
2 6

Output
2
17
7
15
12
11
3
3
4
13
17
8
1
2
18
14
6
6
'''

#YOU SHOULD SAVE YOUR PREVIOUS RESULTS IN DICT 
#SO YOU CAN USE IY TO CALCULATE NEXT RESULTS

import sys

t, r = map(int,sys.stdin.readline().split())
s = list(map(ord, sys.stdin.readline())) 
m = int(sys.stdin.readline())

def fill_hash(s,t,r): #Вынос осн кода в отд ф-ю - ускор 25%
	hash_tbl = [0]
	ts = [1]
	ans = 0
	length = len(s)
	for n in range(length-1):
		ts.append((ts[n]*t)%r)
		ans = (ans*t+s[n])%r #div & sum - done by dift cpu cores
		hash_tbl.append(ans)
	return hash_tbl, ts

def main(s,t,r,m):
	hash_table, ts = fill_hash(s,t,r)
	print(hash_table)
	print(ts)
	for i in range(m):
		a,b = map(int, sys.stdin.readline().split())
		if a == 0:
			print(hash_table[b+1])
		else:
			print((hash_table[b+1] - (ts[b-a+1])*hash_table[a])%r)

main(s,t,r,m)
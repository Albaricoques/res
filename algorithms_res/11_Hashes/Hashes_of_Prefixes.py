''' A. Hashes of Prefixes
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

Polynomial hash of string s of length n is h(s)=(∑(i=0)(n−1) s[i]*t^(n−i−1))*mod(r).
Here, s[i] is the ASCII-code of i-th symbol of string s using 0-indexing. 

For example, for string "abacaba" the hash is calculated as follows: 
(97*t^6+98*t^5+97*t^4+99*t^3+97*t^2+98*t+97)*mod(r).

You are given t, r and string s. Find the hashes of all the prefixes of s.

Input
The first line of the input contains integers t and r (1≤t≤10^9, 2≤r≤10^9).
The second line contains string s (the length of s is in [1,10^5], s consists of only Latin letters).

Output
Let the length of string s be n. Output n integers, one per line, the hashes of strings s[0..0], s[0..1], ..., s[0..n−1].

Example
Input
7 19
abacaba

Output
2
17
7
15
12
11
'''

import sys

t, r = map(int,sys.stdin.readline().split())
s = list(map(ord, sys.stdin.readline()))

def hash(s,t,r): #Вынос осн кода в отд ф-ю - ускор 25%
	ans = 0
	length = len(s)
	for n in range(length-1):
		ans *= t
		ans = (ans+s[n])%r #div & sum - done by dift cpu cores
		print(ans)

hash(s,t,r)

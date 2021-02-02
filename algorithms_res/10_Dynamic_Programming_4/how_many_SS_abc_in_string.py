''' C. ABC
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

A string b=b1b2b3…bm is a subsequence of a string a=a1a2a3…an 
if there is a strictly increasing sequence {i1,i2,i3,…,im} of indices of a, 
such that for all j∈{1,…,m} the following equality holds: aij=bj. 
For example, a string b=abc is a subsequence of a string a=abacaba. 
The corresponding sequence of indices may be, in this case, as follows: {1,2,4}.

You are given a string s consisting of only small English letters. 
Your task is to count the number of ways a string abc occurs as a subsequence in string s.

Input
The single line of the input contains string s. The length of the string is positive and does not exceed 10^5.

Output
Output the number of occurences of abc as a subsequence in the given string.

Examples
abc
#1

ab
#0
'''

import sys

s = sys.stdin.readline()

n = len(s)
c, bc, abc = {n:0}, {n:0}, {n:0}

for i in range(len(s)-1, -1, -1):
	c[i] = c[i+1]

	if s[i]=='c':
		c[i] += 1

	bc[i] = bc[i+1]
	if s[i]=='b':
		bc[i] += c[i]

	abc[i] = abc[i+1]
	if s[i]=='a':
		abc[i] += bc[i]

print(abc[0])

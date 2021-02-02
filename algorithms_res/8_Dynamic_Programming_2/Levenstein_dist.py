''' D. Levenshtein Distance
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

You are given a string. You can perform operations of three types:
    Replace one symbol by another.
    Delete any symbol.
    Insert any symbol in any position of the string. 

The smallest number of operations to be performed in order to transform one string to another one is named edit distance or Levenshtein distance.
Find the Levenshtein distance between two given strings.

Input
The input contains two lines that contain two strings. 
The length of each string does not exceed 1 000 symbols and 
they consist of only uppercase Latin letters.

Output
The sole line of the output should contain the Levenshtein distance between two given strings.

Example
Input
ABCDEFGH
ACDEXGIH

Output
3
'''

import sys

a = sys.stdin.readline().strip() ; b = sys.stdin.readline().strip()

def ld(s, t): 
    m = len(s)
    n = len(t)
    L = [[0 for x in range(n)] for x in range(m)] 
    for i in range(m): 
        for j in range(n): 
            if i == 0 or j == 0: 
                L[i][j] = int(not(s[i] in t[0:j+1] or t[j] in s[0:i+1])) + i + j
            else: 
                L[i][j] = min(L[i-1][j]+1, L[i][j-1]+1, L[i-1][j-1] + (s[i]!=t[j]) )
    if m==0 or n==0:
    	print(m+n)
    else:
	    print(L[i][j])
ld(a,b)
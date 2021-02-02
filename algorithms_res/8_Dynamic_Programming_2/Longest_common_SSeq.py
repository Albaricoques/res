''' C. Longest common subsequence
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

Given two sequences, it is required to find and output their longest common subsequence.

Input
The first line of input contains an integer n (1 ≤ n ≤ 2 000) — the length of the first sequence. 
The second line contains elements of the first sequence (separated by spaces) — integers, not exceeding 10^9 by modulo. 
The third line contains an integer m (1 ≤ m ≤ 2 000) — the length of the second sequence. 
The fourth line contains elements of the second sequence (separated by spaces)  — integers, not exceeding 10^9 by modulo.

Output
The first line of the output should contain the length of the longest common subsequence. 
The second line of the output should contain the longest common subsequence of the sequences itself. 
If there are several answers — output any of them.

Example
Input
3
1 2 3
4
2 3 1 5

Output
2
2 3 
'''

import sys

m = int(sys.stdin.readline()) ; s = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline()) ; t = list(map(int, sys.stdin.readline().split()))

def lcs(X, Y, m, n): 
    L = [[0 for x in range(n+1)] for x in range(m+1)] 
    # Following steps build L[m+1][n+1] in bottom up fashion.
    # L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # Following code is used to print LCS 
    index = L[m][n] 
    # Create a character array to store the lcs string 
    lcs = [""] * (index+1) 
    lcs[index] = "" 
    # Start from the right-most-bottom-most corner and one by one store characters in lcs[] 
    i = m 
    j = n 
    while i > 0 and j > 0: 
        # If current character in X[] and Y are same, then current character is part of LCS 
        if X[i-1] == Y[j-1]: 
            lcs[index-1] = X[i-1] 
            i-=1
            j-=1
            index-=1
        # If not same, then find the larger of two and go in the direction of larger value 
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
  
    print(len(lcs)-1)
    print(*lcs)

lcs(s, t, m, n) 
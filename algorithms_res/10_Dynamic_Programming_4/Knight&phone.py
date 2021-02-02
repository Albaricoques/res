''' D. Knight and Phone
time limit per test: 1 second;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

The chess association decides to distribute to its members special phone numbers 
that can be obtained by the moves of a knight on the following numpad:
1 2 3
4 5 6
7 8 9
  0
For example, 340-49-27 is one of these numbers. 
Please note that a phone number cannot begin with 0 and 8.

Please calculate the number of such phone numbers of length n. 
Since this number can be very large, output it modulo 10^9.

Input
The sole line of the input contains one integer n (1 ≤ n ≤ 100) — the length of the phone numbers.

Output
The sole line of the output should contain one integer — the answer to the problem.

Examples
1
#8

2
#16
'''

import sys

n = int(sys.stdin.readline())

def knightDialer(N):

    moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9],
             [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
    
    result = [0, 1, 1, 1, 1, 1, 1, 1, 0, 1]

    hops = 0

    while hops < N - 1:
        nextResult = [0 for i in range(10)]
        for idx in range(len(result)):
            for step in moves[idx]:
                nextResult[idx] += result[step]
        result = nextResult
        hops += 1

    return( sum(result) % (10**9) )# + 7))

print(knightDialer(n))

''' E. Calculator
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

You are given a calculator that can perform three following operations:
    multiply X by 2;
    multiply X by 3;
    increment X. (X+=1)
Please, count the smallest number of operations to get n from 1.

Input
The sole line of the input contains n(1≤n≤10^6) — the target number.

Output
The sole line of the output should contain one integer — the answer to the problem.
The second line should contain integers that are obtained by applying the operations. 
The first integer should be 1 and the last one should be n. 
If there are several solutions, output any of them.

Examples
1
#0
#1 

5
#3
#1 3 4 5 

962340
#17
#1 3 9 27 54 55 165 495 1485 4455 8910 17820 17821 53463 160389 160390 481170 962340 
'''

import sys

n = int(sys.stdin.readline())

def dp_min_ops(n):
    all_parents = [None] * (n + 1)
    all_min_ops = [0] + [None] * n

    for k in range(1, n + 1):
        curr_parent = k - 1
        curr_min_ops = all_min_ops[curr_parent] + 1

        if k % 3 == 0:
            parent = k // 3
            num_ops = all_min_ops[parent] + 1
            if num_ops < curr_min_ops:
                curr_parent, curr_min_ops = parent, num_ops

        if k % 2 == 0:
            parent = k // 2
            num_ops = all_min_ops[parent] + 1
            if num_ops < curr_min_ops:
                curr_parent, curr_min_ops = parent, num_ops

        all_parents[k], all_min_ops[k] = curr_parent, curr_min_ops

    numbers = []
    k = n
    while k > 0:
        numbers.append(k)
        k = all_parents[k]
    numbers.reverse()

    return all_min_ops, numbers

ans = dp_min_ops(n)[1]
print(len(ans)-1)
print(*ans)

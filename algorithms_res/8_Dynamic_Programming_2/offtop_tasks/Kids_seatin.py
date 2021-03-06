'''
B. Kids Seating
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Today the kindergarten has a new group of n
kids who need to be seated at the dinner table. The chairs at the table are numbered from 1 to 4n. Two kids can't sit on the same chair. It is known that two kids who sit on chairs with numbers a and b (a≠b

) will indulge if:

    gcd(a,b)=1

or,
a
divides b or b divides a

    . 

gcd(a,b)
 — the maximum number x such that a is divisible by x and b is divisible by x

.

For example, if n=3
and the kids sit on chairs with numbers 2, 3, 4, then they will indulge since 4 is divided by 2 and gcd(2,3)=1. If kids sit on chairs with numbers 4, 6, 10

, then they will not indulge.

The teacher really doesn't want the mess at the table, so she wants to seat the kids so there are no 2
of the kid that can indulge. More formally, she wants no pair of chairs a and b

that the kids occupy to fulfill the condition above.

Since the teacher is very busy with the entertainment of the kids, she asked you to solve this problem.
Input

The first line contains one integer t
(1≤t≤100) — the number of test cases. Then t

test cases follow.

Each test case consists of one line containing an integer n
(1≤n≤100

) — the number of kids.
Output

Output t
lines, which contain n distinct integers from 1 to 4n — the numbers of chairs that the kids should occupy in the corresponding test case. If there are multiple answers, print any of them. You can print n

numbers in any order.
Example
Input
Copy

3
2
3
4

Output
Copy

6 4
4 6 10
14 10 12 8

'''

import sys

t = int(sys.stdin.readline())

for case in range(t):
	n = int(sys.stdin.readline())
	ans = [2*n+2]
	step = 2
	while len(ans)<n:
		ans.append(2*n+2*step)
		step += 1
	print(*ans)

#6 8 10 14 16 20 22 

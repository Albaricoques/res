import sys

n = int(input())

stack = list()
mins = list()

for line in sys.stdin:
	if n == 0:
		break
	an = [int(i) for i in line.split()]
	if an[0] == 1:
		stack.append(an[1])
		try:
			mins.append(min(an[1],mins[-1]))
		except:
			mins = [an[1]]
	elif an[0] == 2:
		stack.pop()
		mins.pop()
	else:
		print(mins[-1])
	n -= 1
	
'''
E. Minimum on Stack
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

You have to implement the data structure that supports the following operations:

    1 x — add x to an end of the data structure.
    2 — retrieve the last element from the data structure.
    3 — find the minimal element in the data structure. 

Input

The first line of the input contains one integer n (1≤n≤106) — the number of operations. Next n lines contain the description of operations, one per line. The argument x in an operation of the first type lies in [−109,109] ). It is guaranteed that before retrieval the data structure is not empty.


Output

Output the result for each operation of the third type, one per line.



Example
Input
Copy

8
1 2
1 3
1 -3
3
2
3
2
3

Output
Copy

-3
2
2
'''

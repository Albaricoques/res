stack = list()

def push(x, stack = stack):
	stack.append(x)

def pop(stack = stack):
	stack.pop()

n = int(input())

for i in range(n):
	a = [int(i) for i in input().split()]
	if a[0] == 1:
		stack.append(a[1])
	else:
		print(stack.pop())


'''C. Stack
	time limit per test
	2 seconds
	memory limit per test
	256 megabytes
	input
	standard input
	output
	standard output

	You have to implement a stack with two operations.

	The first operation, push, adds an element to the stack. The second operation, pop, retrieves the element. For each operation of the second type, you should return the retrieved element. It is guaranteed that there always exists an element to retrieve.
	Input

	The first line of the input contains the number of operations 𝑛
	(1≤𝑛≤100000). The next 𝑛 lines describe 𝑛 operations, one per line. The first integer in line is the identifierпервое число: 1 for push, 2 for pop. The second integer is only for push operation — the added element (it does not exceed 100000

	).
	Output

	Output all the retrieved elements in the corresponding order, one per line.
	Example
	Input
	Copy

	6
	1 3
	1 4
	1 6
	2
	1 8
	2

	Output
	Copy

	6
	8
'''

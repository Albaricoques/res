queue_front = {} ; queue_back = {}
q_back_start = {} ; q_front_end = {}

n = int(input())

op = 0
while op < n:
	x = input().split()
	current_queue = x[1]
	if current_queue not in queue_front:
		queue_front[current_queue] = []
		queue_back[current_queue] = []
		q_back_start[current_queue] = 0
		q_front_end[current_queue] = 0

	if len(x)>2:
		if x[0] == 'pushback':
			queue_back[current_queue].append(x[2])
		else:
			queue_front[current_queue].append(x[2])
	else:
		if x[0] == 'popfront':
			try:
				print(queue_front[current_queue].pop())
			except:
				print(queue_back[current_queue].pop(0))
		else:
			try:
				print(queue_back[current_queue].pop())
			except:
				print(queue_front[current_queue].pop(0))
	op += 1

'''E. Dequeues
time limit per test: 2 seconds ; memory limit per test: 256 megabytes
input: standard input ; output: standard output

Write a program that can operate on multiple dequeues.
You should perform four types of operations:
    «pushfront A B» — insert an element B to a front of dequeue A;
    «pushback A B» — insert an element B to an end of dequeue A;
    «popfront A» — retrieve the first elements of dequeue A;
    «popback A» — retrieve the last element of dequeue A. 

Input
The first line contains one integer n (0 ≤ n ≤ 150 000) — the total number of operations.
Each of the next n lines contains a description of an operation. A and B are integers from [1, 150 000].

Output
For each operation popfront or popback output the result on a separate line. It is guaranteed that before the retrieval operation a corresponding dequeue is not empty.

Example
Input
9
pushfront 1 71819
pushback 2 71820
pushback 1 1
popfront 1
popfront 1
pushfront 2 10
pushback 2 11
popback 2
popback 2

Output
71819
1
11
71820

'''

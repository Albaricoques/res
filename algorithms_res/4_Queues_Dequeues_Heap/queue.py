queue = []
n = int(input())
op = 0
q_start = 0
while op < n:
	x = input().split()
	if x[0] == '+':
		queue.append(x[1])
	else:
		print(queue[q_start])
		q_start+=1
	op += 1

'''D. Queue
time limit per test: 2 seconds ; memory limit per test: 256 megabytes
input: standard input ; output: standard output

You have to implement a queue with two operations:
    "+ x" — add an element 𝑥 to the queue;
    "-" — retrieve an element from the queue. 
For each retrieval operation output the result of the operation.

Input
The first line of the input contains the number of operations — 𝑛 (1≤𝑛≤10^5). Next 𝑛 lines contain the description of operations one per line. The added element cannot exceed 10^9.

Output
Output the results of all retrieve operations in the corresponding order, one per line.

Example
Input
4
+ 1
+ 10
-
-

Output
1
10

'''

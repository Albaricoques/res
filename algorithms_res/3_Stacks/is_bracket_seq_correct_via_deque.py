from collections import deque

def iscorrect(seq):

	length = len(seq)
	if length == 0:
		return 'YES'
	if length%2 != 0:
		return 'NO'

	corr = {')':'(',']':'[','}':'{'}
	opening = ['(','{','['] #closing = [')',']','}']

	stack = deque()

	for i in range(length):	
		if seq[i] in opening:
			stack.append(seq[i])
		else:
			l = len(stack)
			if l == 0:
				return 'NO'
			elif corr[seq[i]] != stack.pop():
				return 'NO'

	if len(stack) == 0:
		return 'YES'
	else:
		return "NO"

seq = deque(input())

print(iscorrect(seq))

'''D. Brackets
	time limit per test
	2 seconds
	memory limit per test
	256 megabytes
	input
	standard input
	output
	standard output

	Determine whether the given sequence of round, square and curly brackets is correct.
	
	Input
	The only line of the input file contains 𝑛 brackets in a row (1≤𝑛≤105 ).
	
	Output
	Output "YES", if the given sequence is correct, and "NO" otherwise.
	
	Examples
	Input
	Copy

	()

	Output
	Copy

	YES

	Input
	Copy

	([]){}

	Output
	Copy

	YES

	Input
	Copy

	[]([)]

	Output
	Copy

	NO

	Note

	A bracket sequence is called correct if it can be obtained from any mathematical expression by crossing out all symbols except brackets.

	The formal definition of the correct bracket sequence is:

	    Empty sequence is correct.
	    If A is a regular bracket sequence, then (A), [A] and {A} are regular bracket sequences.
	    If A and B are regular bracket sequences, then AB is a regular bracket sequence. 
'''

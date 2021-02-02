a = input().split()
stack = list()

for i in a:
	if i.isdigit():
		stack.append(int(i))
	elif i == '+':
		stack.append(stack.pop()+stack.pop())
	elif i == '*':
		stack.append(stack.pop()*stack.pop())
	elif i == '-':
		stack.append(-stack.pop()+stack.pop())

print(stack[0])

'''F. Postfix Notation
	time limit per test
	1 second
	memory limit per test
	256 megabytes
	input
	standard input
	output
	standard output

	In a postfix notation (Reverse Polish notation), two operands are followed by an operation. For example, the sum of two numbers A and B is written as A B +. The expression B C + D * means (B + C) * D, and the expression A B C + D * + means A + (B + C) * D. The advantage of a postfix notation is that it does not require brackets and additional operator precedence agreements for its reading.

	An expression is given in the reverse Polish notation. Calculate the result.
	Input

	The input contains the expression in the postfix notation containing single-digit numbers and the operations +, -, *. The string contains no more than 100 numbers and operations.
	Output

	Output the result of the expression. It is guaranteed that the result of the expression, as well as the results of all intermediate calculations is less than 231 by an absolute value.
	Example
	Input
	Copy

	8 9 + 1 7 - *

	Output
	Copy

	-102
'''

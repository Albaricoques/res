'''
K. Square root and square
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Find x such that with the precision at least 6 digits after the point.
Input

The sole line of the input contains one double 1.0 ≤ C ≤ 1010.
Output

The sole line of the output should contain the required x.
Examples
Input
Copy

2.0000000000

Output
Copy

1.0

Input
Copy

18.0000000000

Output
Copy

4.0
'''

C = float(input())
#l = list(range(C))

def func(x):
	return (x**2 + x**0.5)

def f_binary_search(C,f):
	l = 0
	r = C

	for i in range(2000000):#(10):#(2000000):#while abs(f(l)-C)>1e-6 and abs(f(r)-C)>1e-6:
		m = (l+r)/2
		if f(m)>C:
			r=m
		else:
			l=m
		#print(m, l,r)
	#print(f(l),f(r))
	if abs(f(l)-C)<abs(f(r)-C):
		return l
	else:
		return r

print(f_binary_search(C,func))

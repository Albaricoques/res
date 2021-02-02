'''
L. Bridge
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

There was a flood in the town of Graffiti Walls! During the disaster the wooden bridge across the river was demolished. Bipper and his sister Maple were happy to help citizens but that wasn't enough.

Now is your turn to save this wonderful town! There are n new timbers prepared for you and the bridge has to consist of exactly k timbers. You can cut timbers into smaller ones with integer length, but you can't combine them into one, because that would not be solid enough.

Your task is to find maximal width of the bridge.
Input

The first line of input contains two integers n and k (1 ≤ n, k ≤ 10001).

Each of the following n lines contain one integer ai — the length of the i-th timber (1 ≤ ai ≤ 108).
Output

The output must contain one integer — maximal width of the bridge.

If there is no way to make a bridge with the given constraints, answer should be 0.
Example
Input
Copy

4 11
802
743
457
539

Output
Copy

200
'''

n,k = [int(i) for i in input().split()]

a = list()
for i in range(n): #you could try to add some processing here
	a.append(int(input()))
a.sort()

def binary_search(a, k):
	lmax = 1+sum(a)//k
	if lmax == 1:
		return 0
	#print(lmax)
	l,r = 1, lmax
	while l<r-1:
		m = (l+r)//2
		#print('l',l,', r', r,', m', m)
		kk = sum([i//m for i in a])
		#print(kk, k)
		if kk>=k:
			l=m
		else:
			r=m
	return l

if n>1:
	print(binary_search(a,k))
else:
	print(a[0]//k)

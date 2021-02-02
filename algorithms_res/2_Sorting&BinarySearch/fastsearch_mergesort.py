'''
J. Fast search
time limit per test
1 second
memory limit per test
512 megabytes
input
standard input
output
standard output

You are given an array of n
integers a1,a2,…,an

.

Your task is to answer on the queries of the following type: How many items are between l
and r

?.
Input

The first line of the input contains n
 — the length of the array (1≤n≤105

).

The second line contains n
integers a1,a2,…,an (−109≤ai≤109

).

The third line contains integer k
 — number of queries (1≤k≤105

).

The following k
lines contain a pair of integers (l,r) — query, described above (−109≤l≤r≤109

).
Output

The output must consist of k

integers — responses for the queries.
Example
Input
Copy

5
10 1 10 3 4
4
1 10
2 9
3 4
2 2

Output
Copy

5 2 2 0 
'''

def merge(a,b):
    length_a = len(a)
    length_b = len(b)
    c = list() 
    i, j = 0, 0

    while i<length_a and j<length_b:
        if a[i]>b[j]:
            c.append(b[j])
            j+=1
        else:
            c.append(a[i])
            i+=1
    
    if i < length_a:
        c.extend(a[i:])
    if j < length_b:
        c.extend(b[j:])

    return c

def mergesort(a):
    length_a = len(a)
    if length_a == 1:
        return a

    h1 = a[0:length_a//2]
    h2 = a[length_a//2:length_a]

    h1 = mergesort(h1)
    h2 = mergesort(h2)

    return merge(h1,h2)

array_length = input()
a = [int(i) for i in input().split()]
a = mergesort(a)
queries_quantity = int(input())

def binary_search_start(a, start, l, r):
	while l<r:
		m = (l+r)//2
		if a[m]<start:
			l=m+1
		else:
			r=m
	return l

def binary_search_end(a, end, l, r):
	while l<r:
		m = (l+r)//2
		if a[m]>end:
			r=m
		else:
			l=m+1
	return l

lst = list()
for i in range(queries_quantity):
	start, end = [int(i) for i in input().split()]

	l = 0
	r = len(a)


	while l<r: 
		m = (l+r)//2
		if a[m]>end:
			r=m
		elif a[m]<start:
			l=m+1
		else:
			break
			
	start_ind = binary_search_start(a, start, l, m)
	end_ind = binary_search_end(a, end, m, r)
	lst.append(end_ind - start_ind)

print(*lst)

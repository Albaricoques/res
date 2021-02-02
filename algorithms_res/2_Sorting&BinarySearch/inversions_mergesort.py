'''
G. Number of inversions
time limit per test
5 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Given an array A=⟨a1,a2,…,an⟩
of distinct integers. You have to find the number of pairs of indices (i,j) such that i<j and ai>aj

.
Input

The first line of the input contains integer n
(1≤n≤500000) — number of elements in array A

.

The second line contains the elements of the array ai
(0≤ai≤106

) separated by space. No two elements of the array coincide.
Output

Output one integer — the number of inversions in the given array.
Examples
Input
Copy

4
1 2 4 5

Output
Copy

0

Input
Copy

4
5 4 2 1

Output
Copy

6
'''


length = input()
s = [int(i) for i in input().split()]

inversions = 0

def merge(a,b):

    global inversions

    length_a = len(a)
    length_b = len(b)
    #length_ab = length_a + length_b
    #c = [0]*length_ab
    c = list()

    i, j = 0, 0

    while i<length_a and j<length_b:
        if a[i]>b[j]:
            #c[i+j] = 
            c.append(b[j])
            inversions += (length_a-i)
            j+=1
        else:
            c.append(a[i])
            i+=1
    
    if i < length_a:
        c.extend(a[i:])
    if j < length_b:
        c.extend(b[j:])

    return c #, inversions]

def mergesort(a):
    length_a = len(a)
    if length_a == 1:
        return a

    h1 = a[0:length_a//2]
    h2 = a[length_a//2:length_a]

    h1 = mergesort(h1)
    h2 = mergesort(h2)

    return merge(h1,h2)


s = mergesort(s)

#print(s)

print(inversions)


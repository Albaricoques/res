heap = []

def add(x, heap=heap):
    heap.append(x)
    v = len(heap) - 1
    while v>0:
        v2 = (v-1)//2
        if heap[v2]>heap[v]:
            heap[v2], heap[v] = heap[v], heap[v2]
        else:
            break
        v = v2

counter = 0
n = int(input())

for i in range(n):
    an = [int(i) for i in input().split()]
    if an[0] == 0:
        add(an[1])
    else:
        try:
            ans = max(heap)
            ind_ans = heap.index(ans)
        except:
            ind_ans = 0
        print(heap.pop(ind_ans))
    print(heap)


''' I. Heapify
time limit per test: 3 seconds ; memory limit per test: 256 megabytes
input: standard input ; output: standard output

In this problem, you have to implement a data structure that supports two operations:
    insert(x) — add an integer x;
    extract — extract the maximal element. 

Input
The first line of the input contains one integer n (1 ≤ n ≤ 100 000) — the number of performed operations.
Next n lines contain operations, one per line. The operations of the first type have a format "0 x" where 1 ≤ x ≤ 107. The operations of the second type have a format "1".
It is guaranteed that before any operation of the second kind the structure is not empty.

Output
The output should contain the results of extract operations in the corresponding order.

Example
Input
7
0 100
0 10
1
0 5
0 30
0 50
1

Output
100
50
'''
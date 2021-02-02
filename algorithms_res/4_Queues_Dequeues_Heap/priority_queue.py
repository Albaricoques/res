import sys
import heapq as h

heap, history, push_history, push_his_ind_op = [], [], [], []
x = 0 ; pushes = 0 

def extract_min(heap = heap):
    ans = h.heappop(heap) 
    ans_ind = push_history.index(ans)
    push_history[ans_ind] = False
    print(ans, push_his_ind_op[ans_ind]+1) # +1 bc from python which counts from 0
    return

def decrease_key(x, v, heap = heap):
    try:
        number = int(history[x-1][1]) #-1 bc python - from 0
        place = heap.index(number)
    except:
        return
    heap[place] = v
    history[x-1][1] = v
    push_his_ind = history[x-1][2]
    push_history[push_his_ind] = v #-1 bc python - from 0 #800я позиция операции - ЭТО НЕ 800я позиция пуша!!!
    heap = h.heapify(heap)
   

for line in sys.stdin:
    history.append(line.split())
    if history[-1][0] == 'push':
        history[-1].append(pushes)
        pushes += 1
        push_history.append(int(history[-1][1]))
        push_his_ind_op.append(x)
        h.heappush(heap, push_history[-1])
    elif history[-1][0] == 'decrease-key': 
        decrease_key(int(history[-1][1]),int(history[-1][2]))
    elif history[-1][0] == 'extract-min': 
        size = len(heap)
        if size == 0:
            print('*')
        else:
            extract_min()
    x+=1

''' J. Priority queue
time limit per test: 3 seconds ; memory limit per test: 256 megabytes
input: standard input ; output: standard output

Implement a data structure that supports three operations:
    "push 𝑥" — add an element 𝑥;
    "extract-min" — extract the minimal element;
    "decrease-key 𝑖𝑑 𝑣 — decrease an element to 𝑣 added by previous operation 𝑖𝑑. 
If you are asked to decrease an element that was already extracted then you should do nothing.
All operations are enumerated starting from 1.

Input
The input file contains performed operations, one per line. Arguments of push and decrease-key operations do not exceed 10^9 by an absolute value.
It is guaranteed that for any "decrease-key id v" the operation with identifier 𝑖𝑑 is push operation.

Output
For each operation extract-min output two integers on a separate line: the value of the element and the identifier of push operation that added it. If there are several minimal elements, output any of them. If the data structure is empty, output "*".

Example
Input
push 3
push 4
push 2
extract-min
decrease-key 2 1
extract-min
extract-min
extract-min

Output
2 3
1 2
3 1
*
'''
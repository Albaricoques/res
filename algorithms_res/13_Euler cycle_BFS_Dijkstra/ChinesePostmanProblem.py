''' A. Postman
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

There are n squares connected by streets. 
There exists at most three squares with an odd number of adjacent streets. 
Each street is bidirectional and has length. 
There is at least one street and you can travel by streets from any square to any square.

The postman should traverse each street at least once and 
the length of his path should be the smallest possible. 
He can start at any square and finish at any square of his choice.

Input
The first line of the input contains one integer n (1 ≤ n ≤ 1 000) 
— the total number of squares. 
Next n lines describe the streets. 
i-th line contains mi — the number of streets adjacent to the square i. 
This integer is followed by mi pairs of integers. 
j-th pair contains the identifier of the square which is 
the other end of the street and the length of this street.

There can be several streets between two squares, 
but a street cannot connect a square to itself.

All integers in the input do not exceed 10^5.


Output
If the answer exists the first line should contain the total number of streets in a chosen path 
and the second line should contain the identifiers of squares in the order of the path.
If there are no answers, the first line of the output should simply contain -1.
If there are several solutions, output any of them.

Example
4
2 2 1 2 2
4 1 2 4 4 3 5 1 1
2 2 5 4 8
2 3 8 2 4
# 5
# 1 2 4 3 2 1 
'''

import sys
import threading
 
threading.stack_size(48710000)
sys.setrecursionlimit(70000)

answer=list()
n = int(sys.stdin.readline())
ed = [dict() for i in range(n)]
odd=list()
nstrts = 0
for square in range(n):
	streets = list(map(int,sys.stdin.readline().split()))
	nstrts += streets[0]
	if streets[0]%2!=0:
		odd.append(square)
	for street in range(streets[0]):
		if streets[2*street+1]-1 not in ed[square]:
			ed[square][streets[2*street+1]-1]=list()
		ed[square][streets[2*street+1]-1].append(False)

class main():
	def __call__(self):
		global ed, answer,n, odd, nstrts
		if len(odd)==2:
			nstrts = nstrts//2
			print(nstrts)
			self.euler(odd[0])
			for i in answer:
				print(i+1, end=' ')
			print()
		elif len(odd)==0:
			nstrts = nstrts//2
			print(nstrts)
			self.euler(0)
			for i in answer:
				print(i+1, end=' ')
			print()
		else:
			print(-1)

	def euler(self,v):
		global ed, answer
		vs = ed[v].keys()
			if len(ed[v][lastv])>0:
				ed[v][lastv].pop()
				ed[lastv][v].pop()
				self.euler(lastv)
		answer.append(v)

thread = threading.Thread(target=main())
thread.start()
thread.join()

import random
import sys

class TreapNode(object):
	def __init__(self, key):
		self.key = key
		self.ran = random.random()
		self.size = 1 
		self.left = None
		self.right = None
		self.reverse = False

	def left_size(self):
		return 0 if self.left is None else self.left.size

	def right_size(self):
		return 0 if self.right is None else self.right.size

	def recalc(self):
		self.size = self.left_size() + self.right_size() + 1 


class Treap(object):
	def __init__(self):
		self.root = TreapNode(1)

	def split(self, node, key):
		if node == None:
			return (None,None)
		if node.key <= key :
			l,r = self.split(node.right,key)
			node.right = l
			node.recalc()
			return (node,r)
		else:
			l,r = self.split(node.left,key)
			node.left = r
			node.recalc()
			return (l,node)
	
	def merge(self,l,r):
		if l == None:
			return r
		elif r == None:
			return l

		self.push(l)
		self.push(r)

		if l.ran <= r.ran:
			l.right = self.merge(l.right,r)
			l.recalc()
			return l
		else:
			r.left = self.merge(l,r.left)
			r.recalc()
			return r

	def splitK(self, node, size):
		if node == None:
			return (None,None)

		self.push(node)

		if node.left_size() + 1 <= size : #+1?
			node.right, r = self.splitK(node.right, size-node.left_size()-1)
			node.recalc()
			return (node,r)
		else:
			l, node.left = self.splitK(node.left, size)
			node.recalc()
			return (l,node)
	
	def push(self, x):
		if x.reverse:
			l = x.left
			x.left = x.right
			x.right = l
			if not x.left is None:
				x.left.reverse = not x.left.reverse
			if not x.right is None:
				x.right.reverse = not x.right.reverse
			x.reverse = False

	def insert(self,key):
		novo = TreapNode(key)
		self.root = self.merge(self.root,novo)
		
	def rev(self,l,r):
		self.root, R = self.splitK(self.root, r)
		L, self.root = self.splitK(self.root, l-1)
		self.root.reverse = True
		self.push(self.root)
		self.root = self.merge(L, self.root)
		self.root = self.merge(self.root, R)

	def print_list(self):
		self._print_list(self.root)
		print()

	def _print_list(self, node):
		self.push(node)
		if not node.left is None:
			self._print_list(node.left)
		print(node.key, end = ' ')
		if not node.right is None:
			self._print_list(node.right)


t = Treap()
n, m = map(int, input().split())

for i in range(2,n+1):
	t.insert(i)

step = 0
for line in sys.stdin:
	l, r = map(int, line.split())
	t.rev(l,r)
	step += 1
	if step==m:
		break

t.print_list()


''' G. Reverses
time limit per test: 6 seconds ; memory limit per test: 512 megabytes
input: standard input ; output: standard output

You are given an array a1 = 1, a2 = 2, ..., an = n and a sequence of operations: reverse order of elements from position li to position ri.
For example, for array 1, 2, 3, 4, 5, after operation (2, 4), new order will be 1, 4, 3, 2, 5. And then after applying (3, 5) new order will be 1, 4, 5, 2, 3.
Output order of elements after all operations.

Input
First line contains integers n and m (2 ≤ n ≤ 100 000, 1 ≤ m ≤ 100 000) — the number of elements in the array and the number of operations. Next m lines contain the description of operations, one per line. A description consists of two integers li and ri (1 ≤ li ≤ ri ≤ n).

Output
Output n integer numbers — the order of elements in the array, after executing all operations.

Example
Input
5 3
2 4
3 5
2 2

Output
1 4 5 2 3 
'''
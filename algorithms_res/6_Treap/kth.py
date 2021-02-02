import random

class TreapNode(object):
	def __init__(self, key, data):
		self.key = key
		self.ran = random.random()
		self.size = 1
		self.cnt = 1
		self.data = data
		self.left = None
		self.right = None

	def left_rotate(self):
		a = self
		b = a.right
		a.right = b.left
		b.left = a
		a = b
		b = a.left
		b.size = b.left_size() + b.right_size() + b.cnt
		a.size = a.left_size() + a.right_size() + a.cnt
		return a

	def right_rotate(self):
		a = self
		b = a.left
		a.left = b.right
		b.right = a
		a = b
		b = a.right
		b.size = b.left_size() + b.right_size() + b.cnt
		a.size = a.left_size() + a.right_size() + a.cnt
		return a

	def left_size(self):
		return 0 if self.left is None else self.left.size

	def right_size(self):
		return 0 if self.right is None else self.right.size
	
	def __repr__(self):
		return '<node key:%s ran:%f size:%d left:%s right:%s>' % (str(self.key), self.ran, self.size, str(self.left), str(self.right))


class Treap(object):
	def __init__(self):
		self.root = None

	def _insert(self, node, key, data=None):
		if node is None:
			node = TreapNode(key, data)
			return node
		node.size += 1
		if key < node.key:
			node.left = self._insert(node.left, key, data)
			if node.left.ran < node.ran:
				node = node.right_rotate()
		elif key >= node.key:
			node.right = self._insert(node.right, key, data)
			if node.right.ran < node.ran:
				node = node.left_rotate()
		return node

	def insert(self, key, data=None):
		self.root = self._insert(self.root, key, data)
	
	def _find(self, node, key):
		if node == None:
			return None
		if node.key == key:
			return node
		if key < node.key:
			return self._find(node.left, key)
		else:
			return self._find(node.right, key)

	def find(self, key):
		return self._find(self.root, key)

	def _delete(self, node, key):
		if node is None:
			return False
		if node.key == key:
			if node.left is None and node.right is None:
				return None
			elif node.left is None:
				return node.right
			elif node.right is None:
				return node.left
			else:
				if node.left.ran < node.right.ran:
					node = node.right_rotate()
					node.right = self._delete(node.right, key)
				else:
					node = node.left_rotate()
					node.left = self._delete(node.left, key)
		elif key < node.key:
			node.left = self._delete(node.left, key)
		else:
			node.right = self._delete(node.right, key)
		node.size = node.left_size() + node.right_size() + node.cnt
		return node

	def delete(self, key):
		if self.find(key) is None: return False
		self.root = self._delete(self.root, key)
		return True

	def find_kth(self, k):
		if k <=0 or k > self.size():
			return None
		return self._find_kth_subtree(self.root, k-1)
	

	def _find_kth_subtree(self, node, k):
		if k < node.right_size():
			return self._find_kth_subtree(node.right, k)
		elif k > node.right_size():
			return self._find_kth_subtree(node.left, k - node.right_size() - 1) #1 for node itself
		elif k==node.right_size():
			return node.key			

	def size(self):
		return 0 if self.root is None else self.root.size
	
	def median(self):
		s = self.size()
		if s == 0: return 0
		result = 0
		if s % 2 == 1:
			result = self.find_kth(s / 2 + 1).key
		else:
			result = (self.find_kth(s / 2).key + self.find_kth(s / 2 + 1).key) / 2.0
		if result == int(result): result = int(result)
		return result

	def _traverse(self, node):
		if node == None: return
		self._traverse(node.left)
		print(node.key),
		self._traverse(node.right)

	def traverse(self):
		self._traverse(self.root)
	
	def __repr__(self):
		return str(self.root)

t = Treap()

commands = int(input())

for command in range(commands):
	cmd,num = map(int,input().split())
	if cmd==1: 
		t.insert(num)
	elif cmd==-1:
		t.delete(num)
	elif cmd==0:
		print(t.find_kth(num))


''' C. k-th
time limit per test: 2 seconds ; memory limit per test: 512 megabytes
input: standard input ; output: standard output

Write a program that implements a data structure that allows you to add and remove elements, and also find the k-th maximum.

Input
The first line of the input file contains a natural number n(1≤n≤100000) — the number of commands. 
Next n lines contain one command each. The command is written in the form of two numbers ci and ki (|ki|≤10^9) — the type and the argument of the command, respectively. 
Supported Commands:
	+1 (or just 1) : Add an item with the key ki.
	0: Find and print the ki-th maximum.
	-1: Delete the item with the key ki. 

It is guaranteed that the structure is not required to store elements with equal keys or to delete nonexistent elements. It is also guaranteed that when requesting the ki-th maximum, it exists.

Output
Output the result of each command of the second type on a separate line.

Example
Input
11
+1 5
+1 3
+1 7
0 1
0 2
0 3
-1 5
+1 10
0 1
0 2
0 3

Output
7
5
3
10
7
3
'''
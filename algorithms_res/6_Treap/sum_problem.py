import random
#import os

class TreapNode(object):
	def __init__(self, key):#, data):
		self.key = key
		self.ran = random.random()
		self.size = key
		self.left = None
		self.right = None

	def left_size(self):
		return 0 if self.left is None else self.left.size

	def right_size(self):
		return 0 if self.right is None else self.right.size

	def recalc(self):
		self.size = self.key + self.left_size() + self.right_size() 

class Treap(object):
	def __init__(self):
		self.root = None

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
		elif l.ran <= r.ran:
			l.right = self.merge(l.right,r)
			l.recalc()
			return l
		else:
			r.left = self.merge(l,r.left)
			r.recalc()
			return r

	def find(self,t,key):
		if t == None:
			return False
		if t.key == key:
			return True
		elif key < t.key:
			return self.find(t.left,key)
		else:
			return self.find(t.right,key)

	def insert(self,key):
		if self.find(self.root,key):
			return
		novo = TreapNode(key)
		if self.root == None:
			self.root = novo
			return
		L,R = self.split(self.root,key - 1)
		self.root = self.merge(L,novo)
		self.root = self.merge(self.root,R)


	def sum(self,l,r):
		L, self.root = self.split(self.root, l-1)
		self.root, R = self.split(self.root, r)

		if self.root is None:
			ans = 0
		else:
			ans = self.root.size
		self.root = self.merge(L, self.root)
		self.root = self.merge(self.root, R)
		return ans


mod = 10**9
t = Treap()
commands = int(input())
y=0

for command in range(commands):
	cmd = input().split()
	if cmd[0]=='+': 
		t.insert( (int(cmd[1])+y)%mod)
	elif cmd[0]=='?':
		l,r = map(int, cmd[1:3])
		y = t.sum(l,r)
		print(y)
		continue
	y = 0
	

'''D. Sum Problem
time limit per test: 3 seconds ; memory limit per test: 256 megabytes
input: standard input ; output: standard output

Implement a data structure that supports the set of S integers with which the following operations are allowed:
	 — add the number i to the set S (if it is already there, the set does not change);
	 — output the sum of all elements x from S that satisfy the inequality l ≤ x ≤ r. 

Input
Initially, the set S is empty. The first line of the input file contains n — the number of operations (1 ≤ n ≤ 300 000). The next n lines contain operations. Each operation has the form either "+ i" or "? l r". Operation "? l r" sets the query to .
If the operation "+ i" is in the input file at the beginning or after another operation "+", then it defines the operation . If it goes after the query "?", and the result of this query was y, then the operation is performed.
In all queries and adding operations, the parameters are in the range from 0 to 109.

Output
For each request print one number — the response to the request.

Example
Input
6
+ 1
+ 3
+ 3
? 2 4
+ 1
? 2 4
+ 1
+ 2
? 2 4
0

Output
3
7
9
'''
class TreeNode(object): 
	def __init__(self, val): 
		self.val = val 
		self.left = None
		self.right = None
		self.height = 1

class AVL_Tree(object): 

	def find(self,root, key):
		if root is None:
			return 'false'

		if root.val == key:
			return 'true'
		elif root.val > key :
			return self.find(root.left, key)
		else:
			return self.find(root.right, key)

	def next(self, root, key, x=None):
		if root is None:
			if x is None:
				return 'none'
			return x	

		if root.val > key :
			if (x is None) or (root.val < x): 
				x = root.val
			return self.next(root.left, key, x)

		elif root.val <= key:
			return self.next(root.right, key, x)
		
	def prev(self, root, key, x=None):
		if root is None:
			if x is None:
				return 'none'
			return x

		if root.val >= key:
			return self.prev(root.left, key, x)

		elif root.val < key:
			if (x is None) or (root.val > x): 
				x = root.val
			return self.prev(root.right, key, x)
  
	def insert(self, root, key): 
		if not root: 
			return TreeNode(key) 
			

		if root.val == key:
			return root

		elif key < root.val: 
			root.left = self.insert(root.left, key) 
		else: 
			root.right = self.insert(root.right, key) 
  
		# Step 2 - Update the height of the ancestor node 
		root.height = 1 + max(self.getHeight(root.left), 
						  self.getHeight(root.right)) 
  
		# Step 3 - Get the balance factor 
		balance = self.getBalance(root) 
  
		# Step 4 - If the node is unbalanced, then try out the 4 cases 
		# Case 1 - Left Left 
		if balance > 1 and key < root.left.val: 
			return self.rightRotate(root) 
  
		# Case 2 - Right Right 
		if balance < -1 and key > root.right.val: 
			return self.leftRotate(root) 
  
		# Case 3 - Left Right 
		if balance > 1 and key > root.left.val: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 
  
		# Case 4 - Right Left 
		if balance < -1 and key < root.right.val: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 
  
		return root 
  
	# Recursive function to delete a node with given key from subtree with given root. It returns root of the modified subtree. 
	def delete(self, root, key): 
		# Step 1 - Perform standard BST delete 
		if root is None:
			return root
  
		elif key < root.val: 
			root.left = self.delete(root.left, key) 
  
		elif key > root.val: 
			root.right = self.delete(root.right, key) 
  
		else: 
			if root.left is None: 
				
				temp = root.right 
				root = None
				return temp 
  
			elif root.right is None: 
				
				temp = root.left 
				root = None
				return temp 
  
			temp = self.getMinValueNode(root.right) 
			root.val = temp.val 
			root.right = self.delete(root.right, 
									  temp.val) 
  
		# If the tree has only one node, simply return it 
		if root is None: 
			return root 
  
		# Step 2 - Update the height of the ancestor node 
		root.height = 1 + max(self.getHeight(root.left), 
							self.getHeight(root.right)) 
  
		# Step 3 - Get the balance factor 
		balance = self.getBalance(root) 
  
		# Step 4 - If the node is unbalanced, then try out the 4 cases 
		# Case 1 - Left Left 
		if balance > 1 and self.getBalance(root.left) >= 0: 
			return self.rightRotate(root) 
  
		# Case 2 - Right Right 
		if balance < -1 and self.getBalance(root.right) <= 0: 
			return self.leftRotate(root) 
  
		# Case 3 - Left Right 
		if balance > 1 and self.getBalance(root.left) < 0: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 
  
		# Case 4 - Right Left 
		if balance < -1 and self.getBalance(root.right) > 0: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 
  
		return root 
  
	def leftRotate(self, z): 
  
		y = z.right 
		T2 = y.left 
  
		# Perform rotation 
		y.left = z 
		z.right = T2 
  
		# Update heights 
		z.height = 1 + max(self.getHeight(z.left),  
						 self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left),  
						 self.getHeight(y.right)) 
  
		# Return the new root 
		return y 
  
	def rightRotate(self, z): 
  
		y = z.left 
		T3 = y.right 
  
		# Perform rotation 
		y.right = z 
		z.left = T3 
  
		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						  self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						  self.getHeight(y.right)) 
  
		# Return the new root 
		return y 
  
	def getHeight(self, root): 
		if not root: 
			return 0
  
		return root.height 
  
	def getBalance(self, root): 
		if not root: 
			return 0
  
		return self.getHeight(root.left) - self.getHeight(root.right) 
  
	def getMinValueNode(self, root): 
		if root is None or root.left is None: 
			return root 
  
		return self.getMinValueNode(root.left) 
  
	def preOrder(self, root): 
  
		if not root: 
			return
  
		print("{0} ".format(root.val), end="") 
		self.preOrder(root.left) 
		self.preOrder(root.right) 
  
  
myTree = AVL_Tree() 
root = None

import sys

for line in sys.stdin:
	num = int(line.split()[1])
	if line.startswith('insert '):
		root = myTree.insert(root, num)
	elif line.startswith('delete '):
		root = myTree.delete(root, num)
	elif line.startswith('exists '):
		print(myTree.find(root, num))
	elif line.startswith('next '):
		print(myTree.next(root, num))
	elif line.startswith('prev '):
		print(myTree.prev(root, num))


''' C. Balanced binary search tree
time limit per test: 2 seconds ; memory limit per test: 512 megabytes
input: standard input ; output: standard output

Implement a balanced binary search tree.

Input
The input contains several operations with the tree and their amount does not exceed 105. Еvery line contains one of the following operations:
	insert x — insert key x into the tree. If there is a key x in the tree already, do nothing;
	delete x — remove key x from the tree. If there is no key x in the tree, do nothing;
	exists x — if there is a key x in the tree, output "true", otherwise output "false";
	next x — output the smallest key in the tree that is strictly larger than x, or "none" if there's no such key;
	prev x — output the largest key in the tree that is strictly less than x, or "none" if there's no such key. 
All keys are integers no greater than 10^9 by absolute value.

Output
Output results of all operations exists, next, prev.

Example
Input
insert 2
insert 5
insert 3
exists 2
exists 4
next 4
prev 4
delete 5
next 4
prev 4

Output
true
false
5
3
none
3
'''
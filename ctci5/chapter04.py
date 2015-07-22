from __future__ import print_function

class Node(object):

	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

class BinaryTree(object):

	def __init__(self, root=None):
		self.root = root

	def insert(self, key, leaf=None):
		if self.root == None:
			self.root = Node(key)
			return

		if leaf == None: leaf = self.root

		if leaf.data < key:
			if leaf.right != None:
				self.insert(key, leaf.right)
			else:
				leaf.right = Node(key)
		else:
			if leaf.left != None:
				self.insert(key, leaf.left)
			else:
				leaf.left = Node(key)

	def inorder(self, leaf=None):
		if leaf == None: leaf = self.root
		if leaf.left != None: self.inorder(leaf.left)
		print('{} '.format(leaf.data), end="")
		if leaf.right != None: self.inorder(leaf.right)

def main():
	bt = BinaryTree()
	bt.insert(11)
	bt.insert(3)
	bt.insert(7)
	bt.insert(4)
	bt.insert(10)
	bt.insert(9)
	bt.insert(23)
	bt.inorder()
	print("")

if __name__ == "__main__":
	main()


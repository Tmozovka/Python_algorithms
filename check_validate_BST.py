import sys

class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None



def isValidBSTIterative(root: TreeNode):        
	
	"""
	:type root: TreeNode
	:rtype: bool
	"""
	if not root:
		return True

	stack=[(root, -sys.maxsize-1, sys.maxsize),]
	while stack:
		root, lower, upper = stack.pop()
		if root is not None:
			val = root.val
			if val <= lower or val >= upper:
				return False
			stack.append((root.right, val, upper))
			stack.append((root.left, lower, val))

	return True

def isValidBSTRekursive(root):
	"""
	:type root: TreeNode
	:rtype: bool
	"""
	def helper(node, lower = float('-inf'), upper = float('inf')):
		if not node:
			return True
		
		val = node.val
		if val <= lower or val >= upper:
			return False

		if not helper(node.right, val, upper):
			return False
		if not helper(node.left, lower, val):
			return False
		return True

	return helper(root)

def isValidBSTInorderTraversal(root):
	"""
	:type root: TreeNode
	:rtype: bool
	"""
	stack, inorder = [], float('-inf')
	while stack or root:
		while root:
			stack.append(root)
			root = root.left
		root = stack.pop()
		# If next element in inorder traversal
		# is smaller than the previous one
		# that's not BST.
		if root.val <= inorder:
			return False
		inorder = root.val
		root = root.right

	return True

tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(5)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(6)


print(isValidBSTInorderTraversal(tree))
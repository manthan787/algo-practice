class Tree(object):

	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def unival_subtrees(root):
	def unival(root, val, count):
		if not root: return True
		if not root.right and not root.left:
			if root.val == val: return True
			else: return False
		left = unival(root.left, root.val, count)
		right = unival(root.right, root.val, count)
		if left and right and root.val != val:
			print root.val, val
			count[0] += 1
		return True
	count = [0]
	unival(root, root.val, count)
	print count[0]

r = Tree(5, Tree(4, Tree(4), Tree(4)), Tree(2, Tree(2), Tree(2)))
r1 = Tree(5, Tree(4, Tree(4), Tree(4, Tree(4))), Tree(2, Tree(2), Tree(2)))
r2 = Tree(5, Tree(2), Tree(3, Tree(3)))
unival_subtrees(r)
unival_subtrees(r1)
unival_subtrees(r2)
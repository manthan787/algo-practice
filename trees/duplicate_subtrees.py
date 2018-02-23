'''
Given a tree find duplicate subtrees in it
'''

class Tree(object):

	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def duplicate_subtree(root):
	''' Do an inorder traversal and than find similar string '''
	m = {}
	def inorder(root):
		if not root: return []
		s = ["["]
		s += inorder(root.left)
		s.append(str(root.val))
		s += inorder(root.right)
		s.append("]")
		string = ''.join(s)
		if string in m:
			m[string] += 1
		else:
			m[string] = 1
		return s

	inorder(root)
	for s, count in m.iteritems():
		if count > 1:
			print s

r = Tree(4, Tree(2, Tree(4)), Tree(1, Tree(1, Tree(2, Tree(4)))))
r1 = Tree(5)
r1.left = Tree(3, Tree(7, Tree(1), Tree(8)), Tree(3, Tree(1), Tree(2)))
r1.right = Tree(3, Tree(1), Tree(2, Tree(7, Tree(1), Tree(8))))
duplicate_subtree(r)
print "----"
duplicate_subtree(r1)


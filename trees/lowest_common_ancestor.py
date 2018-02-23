class Tree(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))
        return root if left and right else left or right

n1 = Tree(3)
n2 = Tree(4)
r = Tree(1, Tree(2), Tree(5, n1, n2))

node_2 = Tree(2)
r1 = Tree(1, node_2)


s = Solution()
print s.lowestCommonAncestor(r, n1, n2).val
print s.lowestCommonAncestor(r1, r1, node_2).val
class Tree(object):

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """ If p and q are in the same subtree, return root
            of that subtree as the answer
            If both p and q are not in the subtree, return None
            If one of p and q is in the subtree, return that Node
        """
        if not root:
            return root
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


n1 = Tree(3)
n2 = Tree(4)
r = Tree(1, Tree(2), Tree(5, n1, n2))

node_2 = Tree(2)
r1 = Tree(1, node_2)


s = Solution()
print s.lowestCommonAncestor(r, n1, n2).val
print s.lowestCommonAncestor(r1, r1, node_2).val

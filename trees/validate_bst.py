# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev = [None]
        def inorder(node):
            if not node:
                return True
            left = inorder(node.left)
            if prev[0]:
                if node.val < prev[0].val:
                    return False
            prev[0] = node
            right = inorder(node.right)
            return left and right
        return inorder(root)
       

# Tests
s = Solution()
t = TreeNode(2, TreeNode(1), TreeNode(3))
t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(10, t, TreeNode(12, TreeNode(13)))
t3 = TreeNode(10, t, TreeNode(12, TreeNode(10)))
t4 = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))
assert s.isValidBST(t) == True
assert s.isValidBST(t1) == False
assert s.isValidBST(t2) == False
assert s.isValidBST(t3) == True
assert s.isValidBST(t4) == False

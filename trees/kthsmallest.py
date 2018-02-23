'''
Find k-th smallest value in a BST
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.traversals = []
        self.kth = None

    # Solution 1: Do inorder traversal and return Kth element
    #             Complexity: O(n)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inorder(root)
        return self.traversals[k]

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.traversals.append(root.val)
        self.inorder(root.right)

    # Solution 2: At inorder traversal, reduce K by 1, when k is 1
    #             return root; Complexity: O(h)
    def kthSmallest2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inorder2(root, k)
        return self.kth

    def inorder2(self, root, k):
        if not root: return
        self.inorder2(root.left, k)
        if k == 1:
            self.kth = root.val
            return
        k -= 1
        self.inorder2(root.right, k)

s = TreeNode(3)
s.left = TreeNode(1)
s.right = TreeNode(4)
sol = Solution()
print sol.kthSmallest(s, 2)
print sol.kthSmallest2(s, 2)


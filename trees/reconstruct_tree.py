"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
Given preorder and inorder traversal of a tree, construct the binary tree.
"""
class Node(object):

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return "<{}>[{}][{}]".format(self.val, self.left, self.right)


class Solution(object):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return
        root_val = preorder.pop(0)
        # print "Root", root_val, inorder, preorder
        for i, val in enumerate(inorder):
            if val == root_val:
                break
        root = Node(root_val)
        root.left = self.buildTree(preorder, inorder[:i])
        root.right = self.buildTree(preorder, inorder[i + 1:])
        return root
        

s = Solution()
print s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print s.buildTree([3, 1, 2, 4], [1, 2, 3, 4])

# answer = [3, 1, 4, null, 2]

#      3
# 1          4
#     2
#  3 -> 1 4
#  1 -> null, 2

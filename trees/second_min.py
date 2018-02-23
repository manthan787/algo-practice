'''
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
Given a non-empty special binary tree consisting of nodes with the non-negative value,
where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes,
then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all
the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
'''
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: -1
        val = self.helper(root, root.val)
        if val == float("inf"): return -1
        else: return val

    def helper(self, root, val):
        if root.val > val: return root.val
        if root.right and root.left:
            if root.right.val > val:
                return min(self.helper(root.left, val), root.right.val)

            if root.left.val > val:
                return min(self.helper(root.right, val), root.left.val)
            l = self.helper(root.left, val)
            r = self.helper(root.right, val)
            print "Min from left {} is {}".format(root.left.val, l)
            print "Min from right {} is {}".format(root.right.val, r)
            return min(l, r)
        else:
            return float("inf")

t = TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(7), TreeNode(5)))
t1 = TreeNode(2, TreeNode(2), TreeNode(2, TreeNode(7), TreeNode(5)))
t2 = TreeNode(2, TreeNode(2), TreeNode(2))
s = Solution()
print s.findSecondMinimumValue(t1)
print s.findSecondMinimumValue(t2)
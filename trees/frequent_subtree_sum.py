'''
https://leetcode.com/problems/most-frequent-subtree-sum/description/
Given the root of a tree, you are asked to find the most frequent subtree sum.
The subtree sum of a node is defined as the sum of all the node values formed
by the subtree rooted at that node (including the node itself).

So what is the most frequent subtree sum value? If there is a tie,
return all the values with the highest frequency in any order.
'''
from __future__ import print_function

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # populate frequencies of sums by recursively walking the
        # the tree
        frequencies = {}
        self.findTreeSum(root, frequencies)
        res = []
        most_freq = 0
        # Find the most frequent sum here
        for val, freq in frequencies.iteritems():
            if freq > most_freq:
                res = [val]
                most_freq = freq
            elif freq == most_freq:
                res.append(val)
        return res
    
    def findTreeSum(self, root, frequencies):
        ''' Recursively finds sum for each subtree in the tree rooted
            at `root` 
        '''
        if not root: return 0
        left_sum = self.findTreeSum(root.left, frequencies)
        right_sum = self.findTreeSum(root.right, frequencies)
        s = left_sum + right_sum + root.val
        if s in frequencies: frequencies[s] += 1
        else: frequencies[s] = 1
        return s

# Tests
s = Solution()
t = TreeNode(10, TreeNode(20), TreeNode(10))
print(s.findFrequentTreeSum(t))

t = TreeNode(0)
print(s.findFrequentTreeSum(t))

t = TreeNode(5, TreeNode(2), TreeNode(-3))
print(s.findFrequentTreeSum(t))

t = TreeNode(5, TreeNode(2), TreeNode(-5))
print(s.findFrequentTreeSum(t))
"""
https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
"""
from collections import defaultdict


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def findMode(self, root):
        """ O(N) time and O(N) space
        :type root: TreeNode
        :rtype: List[int]
        """
        counts = defaultdict(int)
        maxCount = [0]

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            counts[root.val] += 1
            if counts[root.val] > maxCount[0]:
                maxCount[0] = counts[root.val]
            inorder(root.right)
        inorder(root)
        modes = []
        for val, count in counts.iteritems():
            if count == maxCount[0]:
                modes.append(val)
        return modes

    def findModeConstSpace(self, root):
        """ O(N) time and O(1) space solution """
        ans = []
        if not root:
            return root
        currCount, maxCount, prev = [0], [0], [root.val]

        def findMaxCount(root):
            if not root:
                return
            findMaxCount(root.left)
            if prev[0] == root.val:
                currCount[0] += 1
                if currCount[0] > maxCount[0]:
                    maxCount[0] = currCount[0]
            else:
                currCount[0] = 1
            prev[0] = root.val
            findMaxCount(root.right)

        def findModes(root):
            if not root:
                return
            findModes(root.left)          
            if prev[0] == root.val:
                currCount[0] += 1
            else:
                currCount[0] = 1
            prev[0] = root.val   
            if currCount[0] == maxCount[0]:
                ans.append(root.val)
            findModes(root.right)
        findMaxCount(root)
        currCount, prev = [0], [None]
        findModes(root)
        return ans


s = Solution()
t = TreeNode(2, TreeNode(1), TreeNode(2))
t1 = TreeNode(1, TreeNode(1), TreeNode(2, TreeNode(2), TreeNode(3)))
print s.findModeConstSpace(TreeNode(2, TreeNode(1)))
assert s.findMode(t) == [2]
assert s.findModeConstSpace(t1) == [1, 2]
assert s.findMode(t1) == [1, 2]
assert s.findModeConstSpace(TreeNode(1, None, TreeNode(2)))== [1, 2]
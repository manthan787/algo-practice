'''
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

Given a Binary Search Tree and a target number,
return true if there exist two elements in the BST such that
their sum is equal to the given target.
'''

class Solution(object):
    def findTarget(self, root, k):
        """ Uses BFS
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root: return False
        queue, seen = [root], set()
        while queue:
            n = queue.pop(0)
            if k - n.val in seen: return True
            seen.add(n.val)
            if n.left: queue.append(n.left)
            if n.right: queue.append(n.right)
        return False
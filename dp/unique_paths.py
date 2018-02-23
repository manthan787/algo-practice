'''
https://leetcode.com/problems/unique-paths/description/
'''
import math

class Solution(object):
    def __init__(self):
        self.count = 0

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.path_helper(0, 0, m, n, set())
        return self.count

    def path_helper(self, i, j, m, n, success):
        if (i == m - 1 and j == n - 1): return True
        if (i, j) in success: return True
        if i >= m or j >= n: return False
        res = False
        for a, b in ((i + 1, j), (i, j + 1)):
            if self.path_helper(a, b, m, n, success) and (a, b) not in success:
                self.count += 1
                success.add((a, b))
                if not res: res = True
        return res

s = Solution()
print s.uniquePaths(2, 2)

s1 = Solution()
print s1.uniquePaths(3, 3)

s2 = Solution()
print s2.uniquePaths(1, 10)
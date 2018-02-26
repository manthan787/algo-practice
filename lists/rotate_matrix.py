"""
https://leetcode.com/problems/rotate-image/description/
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        for row in matrix:
            self.reverse(row)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverse(self, row):
        start, end = 0, len(row) - 1
        while start < end:
            row[start], row[end] = row[end], row[start]
            start, end = start + 1, end - 1

s = Solution()
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.rotate(m)
assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

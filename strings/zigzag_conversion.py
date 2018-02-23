'''
Problem: https://leetcode.com/problems/zigzag-conversion/description/
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        rows = [""] * numRows
        i = 0
        while(i < len(s)):
            for x in xrange(numRows):
                if i < len(s):
                    rows[x] += s[i]
                    i += 1
            for x in xrange(numRows - 2, 0, -1):
                if i < len(s):
                    rows[x] += s[i]
                    i += 1
        return "".join(rows)


s = Solution()
print s.convert("PAYPALISHIRING", 3)
print s.convert("ABCDEFGHI", 4)
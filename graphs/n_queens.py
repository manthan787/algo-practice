'''
problem: https://leetcode.com/problems/n-queens/description/

DFS based solution.
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        grid = [["." for i in xrange(n)] for i in xrange(n)]
        results = []
        def solve(row):
            if row == n:
                curr = [""] * n
                for i in xrange(n):
                    curr[i] = "".join(grid[i])
                results.append(curr)
            for column in xrange(n):
                # check if queen can be placed here
                if validPlace(row, column):
                    grid[row][column] = "Q"
                    solve(row + 1)
                    grid[row][column] = "."

        def validPlace(row, column):
            """ Check if placing queen at [row, column] is valid or not"""
            for i in xrange(len(grid)):
                if grid[i][column] == "Q": return False

            diagonals = zip(range(row - 1, -1, -1), range(column + 1, n)) + \
                        zip(range(row - 1, -1, -1), range(column - 1, -1, -1)) + \
                        zip(range(row + 1, n), range(column - 1, -1, -1)) + \
                        zip(range(row + 1, n), range(column + 1, n))

            for x, y in diagonals:
                if grid[x][y] == "Q": return False

            return True

        solve(0)
        return results

s = Solution()
print s.solveNQueens(4)
print s.solveNQueens(8)
print s.solveNQueens(5)

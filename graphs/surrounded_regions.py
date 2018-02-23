'''
https://leetcode.com/problems/surrounded-regions/description/
Given a 2D board containing 'X' and 'O' (the letter O), 
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        m, n = len(board), len(board[0])
        queue = []
        # Add all boundary rows to queue
        for i in xrange(m):
            queue.append((i, 0))
            queue.append((i, n - 1))
        
        # Add all boundary columns to queue
        for i in xrange(1, n - 1):
            queue.append((0, i))
            queue.append((m - 1, i))
        
        while queue:
            i, j = queue.pop()
            if board[i][j] == 'O':
                queue += list(self.get_neighbors(i, j, m, n))
                board[i][j] = 'S'

        for i in xrange(m):
            for j in xrange(n):
                v = board[i][j]
                board[i][j] = 'XO'[v == 'S']

    def get_neighbors(self, i, j, m, n):
        return (c for c in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)] 
                            if 0 <= c[0] < m and 0 <= c[1] < n)


i = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
     ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

s = Solution()
s.solve(i)
print i


i1 = [["X", "X", "X", "X"], ["X", "O", "O", "O"],
     ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
s.solve(i1)
print i1

i2 = []
s.solve(i2)

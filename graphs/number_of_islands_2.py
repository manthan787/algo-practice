class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        islands = 0
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == "1":
                    dfs(grid, i, j, n, m)
                    islands += 1
        return islands

def dfs(grid, i, j, n, m):
    ''' explore the vertex in the grid with given `key` '''
    queue = [(i, j)]
    while queue:
        i, j = queue.pop(0)
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            continue
        queue.append((i - 1, j))
        queue.append((i, j - 1))
        queue.append((i + 1, j))
        queue.append((i, j + 1))
        grid[i][j] = 0

s = Solution()
# print s.numIslands([["0", "0"], ["0", "0"]])
print s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
# print s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
'''
Problem: https://leetcode.com/problems/number-of-islands/description/

Similar code, without any graph datastructure is in `number_of_islands_2.py`.
Interestingly, this code isn't accepted by leetcode, since it exceeds time limit.
I suspect that is due to creating a graph and keeping it in memory. The alternative
solution in `number_of_islands_2.py` avoids creating a graph in memory and it changes
the `grid` in place, so it doesn't require any extra memory for storing `visited` and
other stuff.

Nonetheless, this solution is more readable and maintainable than the other (accepted) one.
'''

class Node(object):

    def __init__(self, key, value, neighbors=None):
        self.value = value
        self.key = key
        self.neighbors = neighbors or []

    def __repr__(self):
        return "{}->{}".format(self.key, self.neighbors)


class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        nodes = self.construct_graph(grid)
        if len(nodes) == 0: return islands
        visited = set()
        for node in nodes:
            if node not in visited:
                visited = bfs(nodes, node, visited)
                islands += 1
        return islands

    def construct_graph(self, grid):
        ''' constructs graph for the given grid with each position in the grid
            represented as a node with neighbors being vertical and horizontal
            adjacent values
        '''
        nodes = {}
        n = len(grid)
        if n == 0: return nodes
        m = len(grid[0])
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == "1":
                    nodes["{}-{}".format(i, j)] = Node("{}-{}".format(i, j), grid[i][j], self.get_neighbor_keys(i, j, n, m))
        return nodes

    def get_neighbor_keys(self, i, j, n, m):
        keys = []
        if i - 1 >= 0 and j >= 0: keys.append("{}-{}".format(i - 1, j))
        if i >= 0 and j - 1 >= 0: keys.append("{}-{}".format(i, j - 1))
        if i + 1 < n and j < m: keys.append("{}-{}".format(i + 1, j))
        if i < n and j + 1 < m: keys.append("{}-{}".format(i, j + 1))
        return keys

def bfs(nodes, key, visited):
    ''' explore the vertex in the grid with given `key` '''
    print "starting at : {}".format(key)
    queue = [nodes[key]]
    while queue:
        node = queue.pop()
        for neighbor in node.neighbors:
            if not nodes.get(neighbor): continue
            if neighbor not in visited:
                queue.append(nodes[neighbor])
        visited.add(node.key)
        print "visited: {}".format(node.key)
    return visited

s = Solution()
print s.numIslands([["0", "0"], ["0", "0"]])
print s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
print s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
print s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])


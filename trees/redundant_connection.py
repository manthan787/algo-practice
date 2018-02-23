'''
https://leetcode.com/problems/redundant-connection/description/
'''
from collections import defaultdict

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        grey = {}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited, grey = set(), {}
        for node in graph:
            if node not in visited:
                self.dfs(node, graph, visited, grey)

    def dfs(self, n, graph, visited, grey):
        grey[n] = True
        visited.add(n)
        for child in graph[n]:
            if child not in visited:
                self.dfs(child, graph, visited, grey)
            if grey.get(child, False):
                print "Cycle {},{}".format(n, child)
        grey[n] = False

s = Solution()
print s.findRedundantConnection([[1,2], [1,3], [2,3]])
print s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])
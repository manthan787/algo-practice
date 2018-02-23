'''
Given a graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's 
set of nodes into two independent subsets A and B
such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes 
j for which the edge between nodes i and j exists.  Each node is an 
integer between 0 and graph.length - 1.  
There are no self edges or parallel edges: graph[i] does not contain i, 
and it doesn't contain any element twice.

Example 1:
Input: [[1, 3], [0, 2], [1, 3], [0, 2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent ubsets.
'''
from __future__ import print_function

class Solution(object):
    def isBipartite(self, graph):
        """
        This problem can be solved using the graph coloring problem.
        For each vertex, assign a color (blue) and to all its adjacent vertices
        assign opposite color (red).
        While traversing the graph, if we come across a case where for any node N
        if any of its children has the same color as N, then it we know it's not 
        a bipartite graph.
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph: return True
        colors = {}
        for node, edges in enumerate(graph):
            node_color = colors.get(node)
            if not node_color:
                colors[node] = 'blue'
            for edge in edges:
                if colors.get(edge) == colors[node]:
                    return False
                else:
                    colors[edge] = ['blue', 'red'][colors[node] == 'blue']
        return True

s = Solution()
assert s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) == True
assert s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) == False
assert s.isBipartite([]) == True
assert s.isBipartite([[1]]) == True

# A forest case where some nodes might not be connected at all
assert s.isBipartite([[4], [], [4], [4], [0, 2, 3]]) == True
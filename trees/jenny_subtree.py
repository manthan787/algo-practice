# Jenny's subtree Problem on HackerRank:
# https://www.hackerrank.com/challenges/jenny-subtrees/problem
import sys

class Node(object):

    def __init__(self, value, neighbors=None):
        self.value = value
        self.neighbors = neighbors or []

    def __repr__(self):
        return "<{}:{}>".format(self.value, self.neighbors)

def build_graph():
    nodes = {}
    n,r = raw_input().strip().split(' ')
    n,r = [int(n),int(r)]
    for a0 in xrange(n-1):
        x,y = raw_input().strip().split(' ')
        x,y = [int(x),int(y)]
        x_node = nodes.get(x, False) or Node(x)
        y_node = nodes.get(y, False) or Node(y)
        if x in nodes:
            nodes[x].neighbors.append(y_node)
        else:
            x_node.neighbors.append(y_node)
            nodes[x] = x_node
        if y in nodes:
            nodes[y].neighbors.append(x_node)
        else:
            y_node.neighbors.append(x_node)
            nodes[y] = y_node
    return n, r, nodes

def bfs(node, r):
    visited = set()
    queue = [node]
    level = 0
    while queue and level < r:
        current = queue.pop(0)
        for n in current.neighbors:
            if n not in visited:
                queue.append(n)
                print current.value, n.value
        visited.add(current)
        level += 1

if __name__ == '__main__':
    n, r, nodes = build_graph()
    for key, node in nodes.iteritems():
        if key == 3: bfs(node, r)
        # bfs(node, r)
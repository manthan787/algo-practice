graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print vertex
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
            print "Stack : " + str(stack)
    return visited

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print vertex
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
            print "Queue : " + str(queue)
    return visited

print dfs(graph, 'A')
print bfs(graph, 'A')
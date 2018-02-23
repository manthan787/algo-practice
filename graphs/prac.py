graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited = set()
    # Put start in the stack already!
    # Why stack though?
    # Well, because we want to immediately visit the children as
    # we encounter them
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in visited:
            # print v
            visited.add(v)
            stack.extend(graph[v] - visited)
    return visited


print dfs(graph, 'A')
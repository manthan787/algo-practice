"""
You are given a list of projects and a list of dependencies 
(which is a list of pairs of projects, where the second project 
is dependent on the  first project). 
All of a project's dependencies must be built before the project is. 
Find a build order that will allow the projects to be built. 
If there is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) 
Output: f, e, a, b, d, c
"""
from collections import defaultdict


def build_order(projects, dependencies):
    colors, dep_graph = {}, defaultdict(list)
    
    for project in projects:
        colors[project] = "white"
    
    for dependency, dependent in dependencies:
        dep_graph[dependent].append(dependency)
    
    ans = []
    for project in projects:
        if colors[project] != 'black':
            ans += create_order(project, dep_graph, colors)
    return ans


def create_order(project, graph, colors):
    colors[project] = "grey"
    order = []
    for dependency in graph[project]:
        if colors[dependency] == 'grey':
            raise Exception("No valid build order exists")
        
        if colors[dependency] == 'white':
            order += create_order(dependency, graph, colors)
    colors[project] = "black"
    order.append(project)
    return order


# Tests
print build_order(
    ['a', 'b', 'c', 'd', 'e', 'f'],
    [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
)

print build_order(
    ['a', 'b', 'c'],
    [('a', 'b'), ('a', 'c')]
)
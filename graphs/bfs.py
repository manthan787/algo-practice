graph = {'A': set(['F', 'B', 'C']),
         'B': set(['A', 'D', 'E', 'G']),
         'C': set(['A', 'F']),
         'D': set(['B', "G"]),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set()}

def bfs(graph, start):
	""" Breadth first search over graph starting at `start`
		we start by putting start in the frontier. And then
		adding neighboring nodes in the frontier.
		All the neighbors are visited before their children.
	"""
	visited = set()
	frontier = []
	frontier.append(start)

	while frontier:
		# Get a node from the frontier
		node = frontier.pop(0)
		for neighbor in graph.get(node, []):
			if neighbor not in visited:
				frontier.append(neighbor)
		visited.add(node)
		print "Visited: {}".format(node)

def bfs_goal(graph, start, goal):
	""" Breadth first search over graph starting at `start`
		we start by putting start in the frontier. And then
		adding neighboring nodes in the frontier.

		All the neighbors are visited before their children.
	"""
	visited = set()
	frontier = []
	came_from = {}
	came_from[start] = None
	d = {}

	for v in graph: d[v] = 1000000
	d[start] = 0
	frontier.append(start)

	while frontier:
		# Get a node from the frontier
		node = frontier.pop(0)
		for neighbor in graph.get(node, []):
			if d[neighbor] > d[node] + 1:
				frontier.append(neighbor)
				came_from[neighbor] = node
				d[neighbor] = d[node] + 1
		visited.add(node)
		print "Visited: {}".format(node)
	return came_from

def construct_path(came_from, goal):
	s = came_from.get(goal)
	path = []
	while s is not None:
		path.append(s)
		s = came_from.get(s)
	print path

# bfs(graph, "A")
construct_path(bfs_goal(graph, "A", "G"), "G")

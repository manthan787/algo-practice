'''
You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate,
return the minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up, left, down, and right.
You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps
required to reach the end is 7, since we would need to go through (1, 2)
because there is a wall everywhere else on the second row.
'''
def min_path(grid, start, end):
    ''' Given a grid, start position and end position, find the shortest path
        to get to end, without going through the walls
    '''
    queue, visited = [start], set([start])
    rows, cols = len(grid), len(grid[0])
    parents, has_path = {}, False
    while queue:
        current = queue.pop(0)
        if end == current:
            has_path = True
            break
        for neighbor in get_neighbors(current, rows, cols):
            if neighbor not in visited and \
                not grid[neighbor[0]][neighbor[1]]:
                parents[neighbor] = current
                queue.append(neighbor)
            visited.add(neighbor)

    if not has_path: return -1
    s, length = end, 0
    path = []
    grid[start[0]][start[1]] = "*"
    while parents.get(s):
        grid[s[0]][s[1]] = "*"
        s = parents[s]
        path.append(s)
        length += 1
    for row in grid:
        print row
    print "\n"
    return length

def get_neighbors(point, rows, cols):
    ''' Get neighbors for a given point in the grid
        Valid neighbors are adjacent left, right, up and down cells
        to a given point
    '''
    neighbors = []
    if point[0] - 1 >= 0: neighbors.append((point[0] - 1, point[1]))
    if point[0] + 1 < rows: neighbors.append((point[0] + 1, point[1]))
    if point[1] - 1 >= 0: neighbors.append((point[0], point[1] - 1))
    if point[1] + 1 < cols: neighbors.append((point[0], point[1] + 1))
    return neighbors

if __name__ == '__main__':
    t, f = True, False
    i1 = [[f, f, f, f],
         [t, t, f, t],
         [f, f, f, f],
         [f, f, f, f]]
    i2 = [[f, f, f, f],
         [t, t, t, t],
         [f, f, f, f],
         [f, f, f, f]]
    i3 = [[f, f, f, f],
         [f, t, t, t],
         [f, f, f, f],
         [f, f, f, f]]
    i4 = [[f, f, t, f],
          [t, f, f, f],
          [f, f, t, f],
          [f, t, f, f]]
    assert min_path(i1, (3, 0), (0, 0)) == 7
    assert min_path(i2, (3, 0), (0, 0)) == -1
    assert min_path(i3, (3, 0), (0, 0)) == 3
    assert min_path(i4, (3, 0), (3, 3)) == 7
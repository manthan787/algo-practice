import heapq
from collections import deque


class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not forest:
            return -1
        heap = self.build_heap(forest)
        path_len, source = 0, (0, 0)
        while heap:
            _, target = heapq.heappop(heap)
            # print "Getting path from {} -> {}{}".format(source, _, target)
            l = self.bfs(forest, source, target)
            if l == -1:
                return -1
            print "Length from {} -> {}{} = {}".format(source, _, target, l)
            path_len += l            
            source = target
        return path_len
    
    def bfs(self, forest, source, target):
        rows, cols = len(forest), len(forest[0])
        queue, length = deque([(source, 0)]), -1
        visited = set()
        while queue:
            curr, l = queue.popleft()
            visited.add(curr)
            if curr == target:
                length = l
                break
            for neighbor in self.get_neighbors(curr, rows, cols):
                neighbor_i, neighbor_j = neighbor[0], neighbor[1]
                if forest[neighbor_i][neighbor_j] and neighbor not in visited:
                    queue.append((neighbor, (l + 1)))
                    visited.add(neighbor)
        # print "Length from {}->{} = {}".format(source, target, length)
        return length

    def a_star(self, forest, source, target):
        rows, cols = len(forest), len(forest[0])
        queue, length = [(0, source, 0)], -1
        heapq.heapify(queue)
        cost_so_far = {}
        cost_so_far[source] = 0
        visited = set()
        while queue:
            _, curr, l = heapq.heappop(queue)
            if curr == target:
                length = l
                break
            for neighbor in self.get_neighbors(curr, rows, cols):
                neighbor_i, neighbor_j = neighbor[0], neighbor[1]
                if forest[neighbor_i][neighbor_j] and neighbor not in visited:
                    neighbor_priority = l + 1 + self.heuristic(neighbor, target)
                    if neighbor_priority < cost_so_far.get(neighbor, 9999):                        
                        cost_so_far[neighbor] = neighbor_priority
                        heapq.heappush(queue, (-neighbor_priority, neighbor, l + 1))
                        visited.add(neighbor)
        # print "Length from {}->{} = {}".format(source, target, length)
        return length
    
    def heuristic(self, node, target):
        x1, y1 = node
        x2, y2 = target
        return abs(x1 - x2) + abs(y1 - y2)

    def build_heap(self, forest):
        rows, cols = len(forest), len(forest[0])
        value_coord = [(forest[i][j], (i, j)) for i in xrange(rows)
                       for j in xrange(cols) if forest[i][j]]
        heapq.heapify(value_coord)
        return value_coord

    def get_neighbors(self, coord, rows, cols):
        x, y = coord[0], coord[1]
        for (i, j) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if i >= 0 and i < rows and j >= 0 and j < cols:
                yield (i, j)


if __name__ == '__main__':
    s = Solution()
    print s.cutOffTree([[1, 2, 3], [0, 0, 4], [7, 6, 5]])
    print s.cutOffTree([
        [1, 2, 3],
        [0, 0, 0],
        [7, 6, 5]
    ])
    print s.cutOffTree([
        [2, 3, 4],
        [0, 0, 5],
        [8, 7, 6]
    ])
    print s.cutOffTree([[54581641, 64080174, 24346381, 69107959], [86374198, 61363882, 68783324, 79706116], [
                       668150, 92178815, 89819108, 94701471], [83920491, 22724204, 46281641, 47531096], [89078499, 18904913, 25462145, 60813308]])

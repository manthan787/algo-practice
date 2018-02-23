'''
https://leetcode.com/problems/network-delay-time/description/
'''
import heapq

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        neighbors, visited = {}, set()
        for u, v, t in times:
            neighbors.setdefault(u - 1, []).append((v - 1, t))
        queue = []
        heapq.heappush(queue, (0, K - 1))
        # Distances of each node from root node (K)
        distances = [float("inf")] * N
        # Set root node's distance to itself as zero
        distances[K - 1] = 0
        while queue:
            _, curr = heapq.heappop(queue)
            for neighbor, time in neighbors.get(curr, []):
                if neighbor not in visited:
                    if distances[neighbor] > time + distances[curr]:
                        distances[neighbor] = time + distances[curr]
                    heapq.heappush(queue, (distances[neighbor], neighbor))
            visited.add(curr)
        print distances
        m = max(distances)
        return m if m != float("inf") else -1

s = Solution()
print s.networkDelayTime([[2,1,3],[2,3,2],[3,4,2]], 4, 2)
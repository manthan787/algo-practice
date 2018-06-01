'''
https://leetcode.com/problems/keys-and-rooms/description/
'''

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if not rooms:
            return True
        visited, stack = set(), [0]
        while stack:
            curr_room = stack.pop()
            visited.add(curr_room)

            for key in rooms[curr_room]:
                if key not in visited:
                    stack.append(key)
        return len(visited) == len(rooms)


s = Solution()
assert s.canVisitAllRooms([[1], [2], [3], []]) == True
assert s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) == False

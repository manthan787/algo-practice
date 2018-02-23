'''
Problem:https://leetcode.com/problems/search-for-a-range/description/
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search(nums, target, i, j):
            '''Find the given value and return index'''
            middle = i + ((j - i) / 2)
            if middle > len(nums) or middle < i: return -1
            if nums[middle] == target:
                while middle >= 0 and nums[middle - 1] == target:
                    middle -= 1
                return middle
            if middle == i: return -1
            if nums[middle] > target:
                return search(nums, target, i, middle)
            else:
                return search(nums, target, middle, j)

        first = search(nums, target, 0, len(nums) - 1)
        if first == -1: return [-1, -1]
        idx = first + 1
        while idx < len(nums) and nums[idx] == target:
            idx += 1
        return [first, idx - 1]

s = Solution()
# print s.searchRange([5,7,7,7,7,8, 8, 8,8,8, 8, 10], 7)
# print s.searchRange([5,7,7,7,7,8, 8, 8,8,8, 8, 10], 13)
print s.searchRange([8, 10], 13)
# print s.searchRange([2,2], 3)
# print s.searchRange([1], 1)

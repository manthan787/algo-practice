"""
https://leetcode.com/problems/degree-of-an-array/description/
"""
from collections import defaultdict

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurrences, degree = defaultdict(list), 0
        for i, num in enumerate(nums):
            occurrences[num].append(i)
            degree = max(degree, len(occurrences[num]))
        min_subarray = len(nums)
        for _, indices in occurrences.iteritems():
            if len(indices) == degree:
                min_subarray = min(indices[-1] - indices[0] + 1, min_subarray)
        return min_subarray


s = Solution()
assert s.findShortestSubArray([1, 2, 2, 3, 1]) == 2
assert s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6

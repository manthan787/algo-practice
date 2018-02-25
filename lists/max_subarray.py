"""
https://leetcode.com/problems/maximum-subarray/description/
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        running_sum = max_sum = nums[0]
        for i in xrange(1, len(nums)):
            # If the current element is bigger than the running sum,
            # we start our subarray from nums[i]
            running_sum = max(running_sum + nums[i], nums[i])

            # Capture the maximum sum across different windows
            max_sum = max(running_sum, max_sum)
        return max_sum

s = Solution()
assert s.maxSubArray([]) == 0
assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert s.maxSubArray([1, 2, 3, 4]) == 10

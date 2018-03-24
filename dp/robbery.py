'''
https://leetcode.com/problems/house-robber/description/
'''

class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [-1] * len(nums)
        return self.helper(nums, 0, memo)

    def helper(self, nums, i, memo):
        if i >= len(nums) or not nums: return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = max(nums[i] + self.helper(nums, i + 2, memo), self.helper(nums, i + 1, memo))
        return memo[i]

    def rob_iter(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        for i in xrange(n - 1, -1, -1):
            dp[i] = max(nums[i] + (dp[i + 2] if i + 2 < n else 0),
                        dp[i + 1] if i + 1 < n else 0)
        return dp[0]


s = Solution()
print s.rob([1, 2, 3, 4])
print s.rob(range(198, 1000, 2))

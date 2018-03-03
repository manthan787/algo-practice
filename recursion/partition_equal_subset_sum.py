"""
https://leetcode.com/problems/partition-equal-subset-sum/description/
"""


class Solution(object):
    def canPartition(self, nums):
        """ This problem is essentially a "subset sum to K" problem.
            But here the target is K/2 (where K = sum of elements of nums).
            If there's a subset of `nums` that sums to sum(nums) / 2, then 
            it means that the other half of `nums` also sums to sum(nums) / 2,
            unless sum(nums) is odd, in which case we can just return False.
        """
        cache = {}

        def helper(nums, i, k):
            if (i, k) in cache:
                return False
            if i >= len(nums):
                return False
            if k == 0:
                return True
            include_curr = helper(nums, i + 1, k - nums[i])
            exclude_curr = helper(nums, i + 1, k)
            if include_curr:
                cache[(i, k)] = False
            return include_curr or exclude_curr
        if not nums:
            return True
        s = sum(nums)
        if s % 2 != 0:
            return False
        return helper(nums, 0, s/2)

    def canPartitionIter(self, nums):
        """ This problem is essentially a "subset sum to K" problem.
            But here the target is K/2 (where K = sum of elements of nums).
            If there's a subset of `nums` that sums to sum(nums) / 2, then 
            it means that the other half of `nums` also sums to sum(nums) / 2,
            unless sum(nums) is odd, in which case we can just return False.
        """
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        dp = [[None for _ in xrange(len(nums) + 1)] for _ in xrange((s/2) + 1)]
        
        for i in xrange(len(nums) + 1):
            dp[0][i] = True

        for i in range(1, (s/2) + 1):
            dp[i][0] = False
        
        for i in xrange(1, (s/2) + 1):
            for j in xrange(1, len(nums) + 1):
                target = i - nums[j - 1]
                if target < 0:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] or dp[target][j - 1]
        return dp[-1][-1]


s = Solution()
assert s.canPartition([]) == True
assert s.canPartitionIter([1, 5, 11, 5]) == True
assert s.canPartitionIter([1, 5, 11, 7]) == True
assert s.canPartitionIter([1, 5, 11, 9]) == False

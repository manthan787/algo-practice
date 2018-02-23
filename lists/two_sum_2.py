'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

Contains three diff solutions:
1) Using binary search - Not time effective
2) Using HashMap - Not space effective
3) Using two pointers - Best
'''

class Solution(object):

    def twoSum(self, numbers, target):
        """ Using two pointers
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        if n <= 1: return None

        i, j = 0, n - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return (i + 1, j + 1)
            elif s > target:
                j -= 1
            else:
                i += 1

    def twoSumDict(self, numbers, target):
        """Two Sum using hashmap
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        ans = None
        for i, num in enumerate(numbers):
            map[num] = i

        for i, num in enumerate(numbers):
            if map.get(target - num):
                return (i + 1, map.get(target - num) + 1)

    def twoSumBinSearch(self, numbers, target):
        """ Two sum using binary search
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        for i, num in enumerate(numbers):
            k = self.search(numbers, 0, len(numbers) - 1, i, target - num)
            if k:
                ans.append((i, k))
        return ans

    def search(self, numbers, i, j, idx, target):
        if not numbers: return None
        if i < 0 or j >= len(numbers): return None
        if i > j: return None
        middle = int(i + j + 1/ 2.)
        if middle != idx and numbers[middle] == target:
            return middle
        elif numbers[middle] > target:
            return self.search(numbers, i, middle - 1, idx, target)
        else:
            return self.search(numbers, middle + 1, j, idx, target)

s = Solution()
print s.twoSumBinSearch([2, 7, 11, 15], 9)
print s.twoSumBinSearch([2, 1, 7], 3)
'''
https://leetcode.com/problems/frog-jump/description/
'''
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        memo = set()
        return self.cross_helper(stones, 0, 0, memo)

    def cross_helper(self, stones, i, prev, memo):
        print memo
        # print stones, stones[i], "Prev Jump:", prev, jumps
        if i >= len(stones): return False
        if i == len(stones) - 1: return True
        prev = stones[i] - prev
        for j in xrange(i + 1, len(stones)):
            next_jump = stones[j] - stones[i]
            if next_jump in (prev - 1, prev, prev + 1):
                if self.cross_helper(stones, j, stones[i], memo) and (i, j, prev) not in memo:
                    return True
            memo.add((i, j, prev))
        return False

s = Solution()
print s.canCross([0, 2])
print s.canCross([0,1,3,5,6,8,12,17])
print s.canCross([0,1,2,3,4,8,9,11])
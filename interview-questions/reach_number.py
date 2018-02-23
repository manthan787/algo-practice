'''
Problem: https://leetcode.com/problems/reach-a-number/description/
'''

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        d = {}
        def attempt(number, move, target):
            if (number, move) in d:
                return d[(number, move)]
            if abs(number) > target: return float("inf")
            print number, move
            if number == target:
                print "Target"
                return move
            incr = attempt(number + (move + 1), move + 1, target)
            decr = attempt(number - (move + 1), move + 1, target)
            d[(number, move)] = min(incr, decr)
            return min(incr, decr)

        def attempt2(target):
            number = 0
            move = 1
            while abs(number) < target:
                number = number + move

        return attempt(0, 0, target)

s = Solution()
# print s.reachNumber(1)
# print s.reachNumber(2)
print s.reachNumber(10)

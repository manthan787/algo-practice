"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        smallest_buying_price, max_profit = prices[0], 0
        for i in xrange(1, len(prices)):
            smallest_buying_price = min(smallest_buying_price, prices[i])
            max_profit = max(max_profit, prices[i] - smallest_buying_price)
        return max_profit


s = Solution()
assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert s.maxProfit([]) == 0

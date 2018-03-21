"""
https://leetcode.com/problems/merge-intervals/description/
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        merged = [sorted_intervals[0]]
        for i in xrange(1, len(intervals)):
            if sorted_intervals[i].start <= merged[-1].end:
                merged[-1].end = max(sorted_intervals[i].end,
                                     merged[-1].end)
            else:
                merged.append(sorted_intervals[i])
        return merged


def equals(intervals, expected):
    for i, inter in enumerate(intervals):
        if (inter.start, inter.end) != expected[i]:
            return False
    return True


s = Solution()
intervals = [Interval(2, 5), Interval(7, 19), Interval(1, 5)]
assert equals(s.merge(intervals), [(1, 5), (7, 19)]) == True
intervals = [Interval(1, 4), Interval(7, 19), Interval(2, 8)]
assert equals(s.merge(intervals), [(1, 19)]) == True
assert s.merge([]) == []

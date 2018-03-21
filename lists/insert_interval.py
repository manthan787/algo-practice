class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def insert(self, intervals, newInterval):
        """ Time complexity: O(3N) """
        if not intervals:
            return [newInterval]
        new_list = []
        for i, interval in enumerate(intervals):
            if interval.start > newInterval.start:
                break
            new_list.append(interval)
        new_list += [newInterval] + intervals[i:]
        merged = [new_list[0]]
        for i in xrange(1, len(new_list)):
            if new_list[i].start <= merged[-1].end:
                merged[-1].end = max(new_list[i].end,
                                     merged[-1].end)
            else:
                merged.append(new_list[i])
        return merged

    def insert_2(self, intervals, newInterval):
        """ Time complexity: O(N), more concise"""
        if not intervals:
            return [newInterval]
        left, right = [], []
        start, end = newInterval.start, newInterval.end
        for inter in intervals:
            if inter.end < start:
                left.append(inter)
            elif inter.start > end:
                right.append(inter)
            else:
                start = min(inter.start, start)
                end = max(inter.end, end)
        return left + [Interval(start, end)] + right

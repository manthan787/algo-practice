"""
https://leetcode.com/problems/find-median-from-data-stream/description/
"""
import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # Min heap stores the minimum element of the second
        # half of the array if it were sorted.
        self.min_heap = []

        # Max heap stores the maximum element of the first
        # half of the array if it were sorted.
        self.max_heap = []

    def addNum(self, num):
        if len(self.max_heap) + len(self.min_heap) <= 1:
            heapq.heappush(self.max_heap, -num)
        else: 
            # if `num` is less than median, put it in max_heap
            # otherwise put it in min_heap
            median = self.findMedian()
            if num < median:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)

        # Rebalance
        # If any of the heaps is bigger than the other heap by 
        # more than 1 element, reabalance.
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        elif len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2.0

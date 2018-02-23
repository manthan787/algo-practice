import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a, b = 0, 0
        s = []
        while a < len(nums1) and b < len(nums2):
            if nums1[a] < nums2[b]:
                s.append(nums1[a])
                a += 1
            else:
                s.append(nums2[b])
                b += 1
        if a < len(nums1):
            for i in xrange(a, len(nums1)):
                s.append(nums1[i])

        if b < len(nums2):
            for i in xrange(b, len(nums2)):
                s.append(nums2[i])
        return self.find_median(s)

    def find_median(self, s):
        if len(s) % 2 != 0:
            return s[(len(s) - 1)/ 2]
        mid = len(s) / 2
        return (s[mid] + s[mid - 1]) / 2


s = Solution()
print s.findMedianSortedArrays([1, 2], [3])
import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        sorted_list = ListNode(0)
        tail = sorted_list
        heap = []
        for l in lists:
            if l: heapq.heappush(heap, (l.val, l))

        while heap:
            val, min_list = heapq.heappop(heap)
            if min_list.next:
                min_list = min_list.next
                heapq.heappush(heap, (min_list.val, min_list))
            tail.next = ListNode(val)
            tail = tail.next
        return sorted_list.next


if __name__ == '__main__':
    s = Solution()
    l0 = ListNode(300)

    l1 = ListNode(1)
    l1.next = ListNode(2)

    l2 = ListNode(3)
    l2.next = ListNode(4)
    h = s.mergeKLists([l0, l1, l2])
    while h:
        print h.val
        h = h.next
'''
Given an array of trips A, where A[K] denotes the destination to be
visited on Kth day, find the shortest vacation of consecutive days
that covers all the unique destinations. It's okay to visit one place
multiple times.

Solution Algorithm:
- Find the total unique destinations in A
- Find the largest index in A that covers all possible destinations and store
  this in a queue
- Now keep removing one element from the front of the queue until the length of the
  queue is equal to unique total destinations
'''
from collections import deque

def solution(A):
    total_destinations = get_total_destinations(A)
    vacation_window, trips = deque([]), dict()
    min_window, i = len(A), 0

    while True:
        if len(vacation_window) <= total_destinations \
            or len(trips) < total_destinations:
            if i >= len(A): break
            vacation_window.append(A[i])
            if A[i] in trips: trips[A[i]] += 1
            else: trips[A[i]] = 1
            i += 1
            print vacation_window
        else:
            v = vacation_window.popleft()
            trips[v] -= 1
            if trips[v] == 0: del trips[v]
            # print "popped", v, trips, vacation_window

        if len(trips) == total_destinations:
            min_window = min(min_window, len(vacation_window))
            if min_window == total_destinations:
                return min_window

    return min_window

def get_total_destinations(trips):
    ''' Given a list of trips, returns total number of
        unique destinations
    '''
    unique_destinations = set()
    for destination in trips:
        unique_destinations.add(destination)
    return len(unique_destinations)


print solution([2, 1, 1, 3, 2, 1, 1, 3])
print solution([7, 3, 7, 3, 1, 3, 4, 1])
print solution([7, 5, 2, 7, 2, 7, 4, 7])
print solution([1, 3, 3, 2, 1])
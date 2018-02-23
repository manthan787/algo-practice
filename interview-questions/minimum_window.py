from collections import deque

def solution(A, T):
    total_destinations = len(T)
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
            print "popped", v, trips, vacation_window

        if len(trips) == total_destinations:
            min_window = min(min_window, len(vacation_window))
            if min_window == total_destinations:
                return min_window

    return min_window


print solution("ADOBECODEBANC", "ABC")
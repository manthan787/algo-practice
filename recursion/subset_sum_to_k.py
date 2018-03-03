"""
Find a subset of elements that sum to K.
S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""
from collections import defaultdict


def find_subset(s, k):
    """ Given a set s, find a subset that sums to k 
        DP Solution: O(KN)
    """
    subset = []
    cache = defaultdict(set)  # cache the subsets that can't make certain sums

    def helper(s, k):
        if k in cache and tuple(s) in cache[k]:
            return False
        if k == 0:
            return True
        if k < 0:
            return False
        if not s:
            return False
        included = helper(s[1:], k - s[0])
        excluded = helper(s[1:], k)
        if included:
            subset.append(s[0])
        else:
            cache[k].add(tuple(s))
        return included or excluded
    helper(s, k)
    return subset


def find_subset_2(s, k):
    """ Given a set s, find a subset that sums to k
        Brute force solution O(N * 2^N)
    """
    subset = []

    def helper(s, k):
        if k == 0:
            return True
        if k < 0:
            return False
        if not s:
            return False
        included = helper(s[1:], k - s[0])
        excluded = helper(s[1:], k)
        if included:
            subset.append(s[0])
        return included or excluded
    helper(s, k)
    return subset


assert find_subset([12, 1, 61, 5, 9, 2], 24) == [2, 9, 1, 12]
assert find_subset([12, 1, 61, 5, 9], 24) == []

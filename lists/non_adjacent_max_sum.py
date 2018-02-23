'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.

For example,
[2, 4, 6, 8] should return 12, since we pick 4 and 8.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.
'''


def largest_non_adjacent(arr):
    if len(arr) <= 2:
        return max(arr)
    return max(largest_non_adjacent(arr[1:]), arr[0] + largest_non_adjacent(arr[2:]))

print largest_non_adjacent([2, 4, 6, 8])
print largest_non_adjacent([5, 1, 1, 5])
def longest_increasing_subsequence(l):
	return helper(l, -10000, 0)

def helper(l, prev, length):
	if not l: return length
	if l[0] > prev:
		include_current, exclude_current = helper(l[1:], l[0], length + 1), \
										   helper(l[1:], prev, length)
		return max(include_current, exclude_current)
	return helper(l[1:], prev, length)

assert longest_increasing_subsequence([]) == 0
assert longest_increasing_subsequence([1, 2, 7]) == 3
assert longest_increasing_subsequence([1, 2, 7, 9, 3, 4]) == 4
assert longest_increasing_subsequence([2, 4, 3, 5, 1, 7, 6, 9, 8]) == 5

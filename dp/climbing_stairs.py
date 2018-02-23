def climb(n, x):
	''' n is number of stairs to climb
		x is the set of number of steps one can climb
		at any step
		returns the number of ways you can climb n steps
		by taking any number of steps from `x`
	'''
	cache = [-1] * n

	def helper(i, n):
		if i == n: return 1
		if i > n: return 0

		if cache[i] != -1:
			return cache[i]
		else:
			res = 0
			for j in x:
				res += helper(i + j, n)
			cache[i] = res
			return res
	if n == 0: return 0
	return helper(0, n)

assert climb(0, [1, 2]) == 0
assert climb(2, [1, 2]) == 2
assert climb(4, [1, 2]) == 5
assert climb(5, [1, 2]) == 8
print climb(3, [1, 3, 5])
print climb(4, [1, 3, 5])
print climb(5, [1, 3, 5])
print climb(500, [1, 2])
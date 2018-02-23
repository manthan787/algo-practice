'''
Find the number of ways that a given integer, X,
can be expressed as the sum of the powers of unique, natural numbers.
'''

def powerSum(x, n):
	return helper(1, x, n)


def helper(i, x, n):
	if i ** n < x:
		return helper(i + 1, x, n) + helper(i + 1, x - i ** n, n)
	elif i ** n == x:
		return 1
	else:
		return 0

print powerSum(10, 2)
print powerSum(100, 2)

# Solution 1: The algorithm Design manual (skienna) way
def is_a_solution(a, k, n):
	return k == n

def construct_candidates(a, k, n):
	return [True, False], 2

def process_solution(a, k):
	s = "{"
	for i in xrange(k+1):
		if a[i]: s += "{}".format(i)
	s += "}"
	print s

def backtrack(a, k, n):
	if is_a_solution(a, k, n):
		process_solution(a, k)
	else:
		k += 1
		candidates, num_candidates = construct_candidates(a, k, n)
		for i in xrange(num_candidates):
			a[k] = candidates[i]
			backtrack(a, k, n)

def generate_subsets(n):
	a = [False]*(n + 1)
	backtrack(a, 0, n)

# generate_subsets(3)

# Solution 2: The pythonic way
def all_subsets(n):
	return helper(0, n)

def helper(i, n):
	res = []
	if i == n: return res
	res.append([i + 1])
	n = helper(i + 1, n)
	for val in n: res.append([i + 1] + val)
	res += n
	return res

print all_subsets(4)














def lcs(s1, s2):
	return helper(s1, s2, 0)

def helper(s1, s2, length):
	# print s1, "->",  s2, length
	if not s1 or not s2: return length
	if s1[0] == s2[0]:
		return helper(s1[1:], s2[1:], length + 1)
	return max(helper(s1[1:], s2, length), helper(s1, s2[1:], length))

assert lcs("", "abc") == 0
assert lcs("", "") == 0
assert lcs("axxxxxxxxxb", "awybbac") == 2
assert lcs("xabzcd", "xvabcd") == 5
assert lcs("xabzc", "vvabcd") == 3

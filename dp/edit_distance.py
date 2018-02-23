def edit_distance(s, p):
	if not s: return len(p)
	if not p: return len(s)
	cost = 0
	if s[-1] == p[-1]:
		cost = edit_distance(s[:-1], p[:-1])
	else:
		cost = 1 + min(edit_distance(s[:-1], p[:-1]),
				   edit_distance(s, p[:-1]),
				   edit_distance(s[:-1], p))
	# print "{}:{} -> {}".format(s, p, cost)
	return cost
print edit_distance("saturday", "sunday")

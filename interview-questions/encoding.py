
def create_lookup():
	return {str(i) : chr(96 + i) for i in xrange(1, 27)}

def find_perms(s):
	lookup = create_lookup()
	for i, c in enumerate(s):
		print lookup[c]
		if i + 1 < len(s):
			print lookup.get(c + s[i + 1], None)

def find(s):
	pass

s = "113457"
find_perms(s)
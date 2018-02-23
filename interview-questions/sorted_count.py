def count(l, target):
	n = len(l)

	f = first(l, 0, n, target)
	l = last(l, 0, n, target)

	def first(a, start, end, target):
		mid = (end + start) / 2
		if end > start:
			pass
		return -1

	def last(a, start, end, target):
		mid = (end + start) / 2
		if end > start:
			pass
		return -1

count([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3], 3)


'''
Given two singly linked lists that intersect at some point, find the intersecting node.
The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

class Node(object):

	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def __repr__(self):
		return "Node({})".format(self.value)


def intersection(a, b):
	'''
	given two linked lists `a` and `b` return the intersection
	node of two
	example,
		a = 3 -> 7 -> 8 -> 10
		b = 99 -> 1 -> 8 -> 10,
		return the node with value 8.
	'''
	a_len = get_list_length(a)
	b_len = get_list_length(b)
	offset = abs(a_len - b_len)
	if a_len > b_len:
		for _ in xrange(offset):
			if not a: return None
			a = a.next
	else:
		for _ in xrange(offset):
			if not b: return None
			b = b.next

	while a and b:
		if a.value == b.value: return a
		a, b = a.next, b.next
	return None

def get_list_length(l):
	''' given a linked list `l` return the length `l` '''
	tmp = l
	length = 0
	while tmp:
		length += 1
		tmp = tmp.next
	return length

l1 = Node(3, Node(7, Node(8, Node(10))))
l2 = Node(99, Node(1, Node(8, Node(10))))
l3 = Node(7, Node(8, Node(10)))
l4 = Node(99, Node(1, Node(8, Node(10))))

print intersection(l1, l2)
print intersection(l3, l4)
print intersection(l4, l3)
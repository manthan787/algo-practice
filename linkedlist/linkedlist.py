class Linkedlist(object):

	def __init__(self):
		self.head = None
		self.tail = None

	def make(self, l):
		''' Takes a list `l` and creates a linked list out of it '''
		for v in l:
			if not self.head:
				self.head = Node(v)
				self.tail = self.head
			else:
				n = Node(v)
				self.tail.next = n
				self.tail = n
		return self.head

class Node(object):

	def __init__(self, value):
		self.value = value
		self.next = None

	def append(self, value):
		n = Node(value)
		if tail: tail.next = n
		else: tail = n

	def __str__(self):
		return "Node({}) -> {}".format(self.value, self.next)
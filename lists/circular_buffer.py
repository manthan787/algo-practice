'''
You run a sneaker website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
'''

'''
Circular Buffer with size = `max_size`
'''
class CircularBuffer(object):

	def __init__(self, max_size):
		self.max_size = max_size
		self.current = 0
		self.buffer = []

	def add(self, value):
		if len(self.buffer) == self.max_size:
			self.buffer[self.current] = value
		else:
			self.buffer.append(value)
		self.current = (self.current + 1) % self.max_size
		print "Index {} after adding {}".format(self.current, value)

	def get_last(self, i):
		print "Fetching from {}".format(self.current - i)
		return self.buffer[self.current - i]

if __name__ == '__main__':
	buffer = CircularBuffer(5)
	buffer.add(1)
	buffer.add(2)
	buffer.add(3)
	buffer.add(4)
	buffer.add(5)
	buffer.add(6)
	buffer.add(7)
	print buffer.buffer
	print buffer.current
	print buffer.get_last(4)

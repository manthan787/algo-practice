'''
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack.
       If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently.
       If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
'''

class Stack(object):

    def __init__(self):
        # Stack for actual values
        self.values = []

        # Stack for max values
        # In this we only keep values that are max
        # at each step
        self._max = []

    def push(self, val):
        self.values.append(val)
        if self._max:
            self._max.append(max(val, self._max[-1]))
        else:
            self._max.append(val)

    def pop(self):
        popped = self.values.pop()
        self._max.pop()
        return popped

    def max(self):
        if not self._max:
            raise Error("No elements in the stack!")
        else: return self._max[-1]

s = Stack()
for i in xrange(5):
    s.push(i)

for i in xrange(5):
    print "Max", s.max()
    print "Popped", s.pop()
'''
https://leetcode.com/problems/min-stack/description/

 Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self._min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.values.append(x)
        if self._min:
            self._min.append(min(x, self._min[-1]))
        else:
            self._min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self._min.pop()
        return self.values.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.values[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min[-1]

s = MinStack()
s.push(-1)
s.push(9)
s.push(2)

print "Min", s.getMin()

s.pop()
s.pop()

print "Min", s.getMin()
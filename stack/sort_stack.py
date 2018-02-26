"""
Write a program to sort a stack such that the smallest items are on the top. 
You can use an additional temporary stack, but you may not copy the elements 
into any other data structure (such as an array). 

The stack supports the following operations: push, pop, peek, and isEmpty.
"""


class Stack(object):

    def __init__(self):
        self.sorted_stack = []
        self.tmp_stack = []

    def push(self, val):
        if not self.sorted_stack:
            self.sorted_stack.append(val)
            return

        if val < self.sorted_stack[-1]:
            self.sorted_stack.append(val)
        else:
            # Maintain the sorted stack invariant
            while self.sorted_stack and self.sorted_stack[-1] < val:
                removed = self.sorted_stack.pop()
                self.tmp_stack.append(removed)
            self.sorted_stack.append(val)

            # Restore all the moved values back on top of the
            # sorted stack
            while self.tmp_stack:
                self.sorted_stack.append(self.tmp_stack.pop())

    def pop(self):
        if not self.isEmpty():
            return self.sorted_stack.pop()
        raise Exception("Calling pop on empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.sorted_stack[-1]
        raise Exception("Calling peek on empty stack")
    
    def isEmpty(self):
        return not len(self.sorted_stack) > 0


s = Stack()
for val in [7, 8, 2, 13, 4]:
    s.push(val)
assert s.peek() == 2
assert s.pop() == 2
assert s.pop() == 4
assert s.pop() == 7
assert s.pop() == 8
assert s.pop() == 13
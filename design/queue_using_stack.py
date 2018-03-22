class MyQueue(object):

    def __init__(self):
        self.values, self.temp = [], []
        self.front = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.values.append(x)
        if len(self.values) == 1:
            self.front = x

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.values) > 1:
            self.temp.append(self.values.pop())
        popped = self.values.pop()
        while self.temp:
            self.push(self.temp.pop())
        return popped

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.values

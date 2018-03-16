"""
Build a hit counter that shows the hit counts for last five minutes.
Implement following methods:
log_hits() -> Log incoming hits
get_hits() -> Get the total number of hits in last five minutes
"""
from time import time, sleep


class Node(object):

    def __init__(self, count=0, next_=None, time_=None):
        self._count = count
        self._next = next_
        self._time = time_


class Log(object):

    def __init__(self, expiration=5):
        self.root = Node()
        self.last = self.root
        self.expiration = expiration
        self._init_list()

    def _init_list(self):
        curr = self.root
        for _ in xrange(299):
            n = Node()
            curr._next = curr = n
        curr._next = self.root

    def log_hit(self):
        curr_time = time()
        if self.last._time == curr_time:
            self.last._count += 1
            return
        self.last = self.last._next
        self.last._count += 1
        self.last._time = curr_time

    def get_hits(self):
        curr_time, curr_ptr = time(), self.last
        hits = 0
        while curr_ptr._next != self.last:
            if curr_ptr._time and curr_ptr._time - curr_time <= self.expiration * 60:
                print curr_ptr._time - curr_time
                hits += curr_ptr._count
            curr_ptr = curr_ptr._next
        return hits

    def print_list(self):
        curr_ptr = self.root
        s, c = "", 0
        while curr_ptr._next != self.root:
            s += "|{}, {}| ->".format(curr_ptr._count, curr_ptr._time)
            curr_ptr = curr_ptr._next
            c += 1
        print s, c


log = Log(expiration=0.2)
for i in xrange(10):
    log.log_hit()
log.print_list()
# sleep(13)
for i in xrange(10):
    log.log_hit()
log.print_list()
print log.get_hits()

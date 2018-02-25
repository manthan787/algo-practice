"""
LRU implementation with linkedlist and dict
"""


class LinkedListNode(object):

    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return "<{}:{}>".format(self.key, self.value)


class DoublyLinkedList(object):

    def __init__(self):
        self.head = LinkedListNode(0, 0)
        self.tail = LinkedListNode(0, 0)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def append_new(self, key, value):
        """ Given `key` and `value` create a LinkedListNode 
            and append to the list
        """
        n = LinkedListNode(key, value)
        self.append(n)
        return n

    def append(self, node):
        """ Given a `node` append it to the list """
        prev = self.tail.prev
        prev.next = self.tail.prev = node
        node.prev, node.next = prev, self.tail

    def remove(self, node):
        """ Remove the given `node` from the list """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def pop(self):
        """ Pop the first element of the list that is not the head or tail.
            This element represents the least recently used element in the 
            LRUCache
        """
        if self.head.next != self.tail:
            n = self.head.next
            self.remove(self.head.next)
            return n


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity

        # Store the cache pages in a doubly linked list based
        # queue, where the least recently used node is the first
        # node in the queue
        self.pages = DoublyLinkedList()

        # Store the corresponding linkedlist node to each
        # key in cache
        self.cache = dict()

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.pages.remove(node)
            self.pages.append(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.pages.remove(self.cache[key])

        elif len(self.cache) >= self.capacity:
            # Remove the least recently used element from the
            # doubly linked list (in this case, the first element)
            p = self.pages.pop()

            # Remove the node entry from cache dict as well
            del self.cache[p.key]
            print "Popped Least Recently Used node: {}".format(p)
        self.cache[key] = self.pages.append_new(key, value)


cache = LRUCache(3)
cache.put("hello", "world")
cache.put("abc", "123")
cache.get("hello")
cache.put("abc", "nsblnb")
cache.put("new", "nsblnb")
cache.put("new1", "nsblnb")

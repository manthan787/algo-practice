"""
Implement a data structure supporting the following operations:

    Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. 
               Key is guaranteed to be a non-empty string.
    Dec(Key) - If Key's value is 1, remove it from the data structure. 
               Otherwise decrements an existing key by 1. 
               If the key does not exist, this function does nothing. 
               Key is guaranteed to be a non-empty string.
    GetMaxKey() - Returns one of the keys with maximal value. 
                  If no element exists, return an empty string "".
    GetMinKey() - Returns one of the keys with minimal value. 
                  If no element exists, return an empty string "".

Challenge: Perform all these in O(1) time complexity. 
"""
from collections import defaultdict


class LinkedListNode(object):

    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

    def remove_from_bucket(self, k):
        self.value.remove(k)

    def add_to_bucket(self, k):
        self.value.add(k)

    def __repr__(self):
        return "<{}:{}>".format(self.key, self.value)


class DoublyLinkedList(object):

    def __init__(self):
        self.front = LinkedListNode(0, 0)
        self.rear = LinkedListNode(0, 0)
        self.front.next = self.rear
        self.rear.prev = self.front

    def insert_before(self, node, node_after):
        prev = node_after.prev
        prev.next = node_after.prev = node
        node.prev, node.next = prev, node_after
    
    def insert_after(self, node, node_before):
        self.insert_before(node, node_before.next)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def get_first(self):
        if self.front.next != self.rear:
            return self.front.next
        return None
    
    def get_last(self):
        if self.rear.prev != self.front:
            return self.rear.prev
        return None
    
    def print_(self):
        curr = self.front
        while curr != self.rear:
            print curr
            curr = curr.next


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(int)
        self.min_max = DoublyLinkedList()
        self.node_map = {0: self.min_max.front}
    
    def add_new_node(self, key):
        new_node = LinkedListNode(key, set())
        self.node_map[key] = new_node
        return new_node
    
    def list_cleanup(self, key):
        if not self.node_map[key].value:
            self.min_max.remove(self.node_map[key])
            del self.node_map[key]

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        prev_count = self.data[key]
        self.data[key] += 1
        count = self.data[key]        
        if count not in self.node_map:
            new_node = self.add_new_node(count)
            self.min_max.insert_after(new_node, self.node_map[prev_count])
        
        if prev_count > 0:
            self.node_map[prev_count].remove_from_bucket(key)
            self.list_cleanup(prev_count)

        node = self.node_map[count]
        node.value.add(key)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.data:
            return
        if self.data[key] == 1:
            self.node_map[1].remove_from_bucket(key)
            del self.data[key]
            self.list_cleanup(1)
        else:
            prev_count = self.data[key]
            self.data[key] -= 1
            count = prev_count - 1            
            if count not in self.node_map:
                new_node = self.add_new_node(count)
                self.min_max.insert_before(new_node, self.node_map[prev_count])
            
            if prev_count > 0:
                self.node_map[prev_count].remove_from_bucket(key)
                self.list_cleanup(prev_count)

            node = self.node_map[count]
            node.value.add(key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if not self.data:
            return ""
        keys = list(self.min_max.get_last().value)
        if not keys:
            return ""
        return keys[0]

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if not self.data:
            return ""
        keys = list(self.min_max.get_first().value)
        if not keys:
            return ""
        return keys[0]


a_one = AllOne()
a_one.inc("a")
a_one.inc("b")
a_one.inc("b")
a_one.inc("c")
a_one.inc("c")
a_one.inc("c")
a_one.dec("b")
a_one.dec("b")
# print a_one.min_max.print_()
print a_one.getMinKey()
a_one.dec("a")
print a_one.getMaxKey()
print a_one.getMinKey()


"""
Design an LRU cache with following API:

get(key) - Return the value for the given key if it exists in the cache,
           otherwise return -1
put(key, value) - Set the value `value` for given `key`. If the cache has
                  reached its capacity, discard the key-value added least
                  recently and add `key` -> `value`
"""
from collections import OrderedDict


class LRUCache(object):
    """ LRU Cache using OrderedDict """

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """ Get the corresponding value for given `key` """
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        return -1

    def put(self, key, value):
        """ Set value to `value` for given `key`.
            If the cache has reached its capacity, discard the least
            recent entry and add the given `key` - `value` pair
        """
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        elif len(self.cache) >= self.capacity:
            _ = self.cache.popitem(last=False)
            # print "Discarded least recent kv pair: {}".format(_)
        self.cache[key] = value


cache = LRUCache(3)
cache.put("hello", "world")
cache.put("abc", "123")
cache.get("hello")
cache.put("s,bn", "nsblnb")
cache.put("yuoiux", "nsblnb")
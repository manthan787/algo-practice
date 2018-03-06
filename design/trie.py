"""
Implement a trie with insert, search, and startsWith methods.
"""


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word:
            return
        if word[0] not in self.data:
            self.data[word[0]] = {}
        curr = self.data[word[0]]
        for i in xrange(1, len(word)):
            if word[i] not in curr:
                curr[word[i]] = {}
            curr = curr[word[i]]
        curr["__end__"] = "__end__"

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if word[0] not in self.data:
            return False
        curr = self.data[word[0]]
        for i in xrange(1, len(word)):
            if word[i] not in curr:
                return False
            curr = curr[word[i]]
        if "__end__" in curr:
            return True
        return False 

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype:
        """
        if not prefix:
            return False
        if prefix[0] not in self.data:
            return False
        curr = self.data[prefix[0]]
        for i in xrange(1, len(prefix)):
            if prefix[i] not in curr:
                return False
            curr = curr[prefix[i]]
        return True

# Tests
t = Trie()
t.insert("hello")
t.insert("helix")
t.insert("cat")
t.insert("carrot")
assert t.search("hello") == True
assert t.search("Hello") == False
assert t.search("cat") == True
assert t.search("carrot") == True
assert t.search("zzzy") == False
assert t.startsWith("car") == True

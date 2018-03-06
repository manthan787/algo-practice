"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

Example Usage:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""


class WordDictionary(object):
    """ This implementation uses Trie """

    def __init__(self):
        self.data = {}

    def addWord(self, word):
        """ Inserts a word into the trie. """
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
        """ Returns if the word is in the data structure. 
            A word could contain the dot character '.' to represent any one letter.
        """
        return self.match(word, self.data)

    def match(self, word, node):

        # If we have read all the letters of the word,
        # then check whether the trie has __end__ node 
        # in it.
        if not word: 
            if "__end__" in node:
                return True
            else:
                return False

        # If the word contains ".", then try all the possible
        # neighbors of `node` and try to match them (recurse!)
        if word[0] == ".":
            for child in node:
                if self.match(child + word[1:], node):
                    return True
            return False
        
        # If there's no node with first letter of the word (or a substring)
        # return False
        if word[0] not in node:
            return False
        
        # We know that the first letter is in the Trie, so recurse on the
        # remaining letters
        return self.match(word[1:], node[word[0]])


wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
assert wd.search("pad") ==  False
assert wd.search("bad") == True
assert wd.search(".ad") == True
assert wd.search("b..") == True
assert wd.search("") == False

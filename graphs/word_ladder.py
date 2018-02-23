'''
https://leetcode.com/problems/word-ladder/description/
'''

from collections import deque

class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList: return 0
        positions = self.process_dictionary(wordList)
        queue = deque([(beginWord, 1)])
        seen = set()
        while queue:
            curr, level = queue.popleft()
            if curr == endWord:
                return level

            for possible_word in self.get_transformations(curr, positions, wordList):
                if possible_word not in seen:
                    queue.append((possible_word, level + 1))
                    seen.add(possible_word)
        return 0

    def process_dictionary(self, wordList):
        ''' Process dictionary and store possible words
            at each location
        '''
        positions = {}
        for word in wordList:
            for i, letter in enumerate(word):
                positions.setdefault(i, set()).add(letter)
        return positions

    def get_transformations(self, word, positions, wordList):
        ''' Get possible one letter transformations given a word '''
        for i, _ in enumerate(word):
            for possible_letter in positions.get(i, []):
                w = word[0:i] + possible_letter + word[i + 1:]
                if w in wordList:
                    wordList.remove(w)
                    yield w

s = Solution()
print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log", "cog"])
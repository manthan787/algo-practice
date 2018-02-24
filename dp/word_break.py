"""
Problem: https://leetcode.com/problems/word-break/description/
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """        
        if not s: return False
        if not wordDict: return False
        # Memo memoizes the words that are not breakable
        # So that we don't end up repeating the same work
        # again an again
        wordDict, memo = set(wordDict), set()
        def can_break(s):
            if not s: return True
            if s in memo: return False
            for i, _ in enumerate(s):
                word = s[:i + 1]
                if word in wordDict:
                    if can_break(s[i + 1:]): 
                        return True
                    else:
                        memo.add(word)
            memo.add(s)
            return False
        return can_break(s)


s = Solution()
assert s.wordBreak("leetcode", ["leet", "code", "le"]) == True
assert s.wordBreak("leetcod", ["leet", "code", "le", "et", "cod"]) == True
assert s.wordBreak("abc", ["a", "b", "et", "cod"]) == False
assert s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaa", ["a", "aa", "aaa", "aaaa", "aaaaa"]) == True

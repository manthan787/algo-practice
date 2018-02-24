"""
problem: https://leetcode.com/problems/word-break-ii/description/
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return []
        if not wordDict:
            return []
        # Memo memoizes the words that are not breakable
        # So that we don't end up repeating the same work
        # again an again
        wordDict, memo = set(wordDict), set()

        def find_breakable_words(s):
            if not s:
                return [""]
            if s in memo:
                return []
            res = []
            for i, _ in enumerate(s):
                word = s[:i + 1]
                if word in wordDict:
                    all_breakable_words = find_breakable_words(s[i + 1:])
                    if not all_breakable_words:
                        memo.add(s[i + 1:])
                    for v in all_breakable_words:
                        res.append((word + " " + v).strip())
            if not res:
                memo.add(s)
            return res
        return find_breakable_words(s)


s = Solution()
assert s.wordBreak("leetcode", ["leet", "code", "le", "et"]) == [
    'le et code', 'leet code']
assert s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) == [
    'cat sand dog', 'cats and dog']
assert s.wordBreak("", ["hello"]) == []
assert s.wordBreak("leetcode", []) == []
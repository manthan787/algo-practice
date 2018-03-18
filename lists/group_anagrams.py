"""
https://leetcode.com/problems/group-anagrams/description/
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        anagrams = defaultdict(list)
        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        return anagrams.values()


s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

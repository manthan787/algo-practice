'''
Problem: https://leetcode.com/problems/interleaving-string/description/
'''

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        states = {}
        states[s1[0]] = set([s2[0], s1[1]])
        states[s2[0]] = set([s1[0], s2[1]])
        states[s1[-1]] = set()
        states[s2[-1]] = set()
        for i in xrange(1, len(s1)):
            states.setdefault(s1[i - 1], set()).add(s1[i])
            if i < len(s2):
                states[s1[i  - 1]].add(s2[i - 1])
            print i, states

        for i in xrange(1, len(s2)):
            states.setdefault(s2[i - 1], set()).add(s2[i])
            if i < len(s1):
                states[s2[i  - 1]].add(s1[i - 1])

        if s3[0] != s1[0] and s3[0] != s2[0]:
            return False
        print states
        for i in xrange(1, len(s3)):
            expected = states[s3[i - 1]]
            if not expected: return True
            if s3[i] not in expected:
                print i, s3[i], expected
                return False
        return True

s = Solution()
print s.isInterleave("abc", "def", "adebcf")
print s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
print s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
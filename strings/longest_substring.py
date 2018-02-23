'''
Longest substring without repeating characters:
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

"abcabcbb" => 3 ("abc")
"bbbbb" => 1 ("b")
"pwwkew" => 3 ("wke")
'''
def longest_substring(s):
    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)
        used[c] = i
    return max_length

assert longest_substring("abcabcbb") == 3
assert longest_substring("bbbb") == 1
assert longest_substring("pwwkew") == 3
def count_palindrome(s):
    res = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i : j+1] == s[i : j+1][::-1]:
                res += 1
    return res

print count_palindrome("hellolle")
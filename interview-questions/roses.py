def solution(P, K):
	if K == 1: return 1
	s = [0]*len(P)
	for i in xrange(len(P)):
		s[P[i] - 1] = i + 1
	j = 0
	stack = []
	ans = -1
	while j < len(s):
		while stack:
			if j - stack[-1] - 1 == K:
				if ans == -1 or ans > max(s[j],s[stack[-1]]):
					ans = max(s[j],s[stack[-1]])
			if s[stack[-1]] > s[j]:
				stack.pop()
			else: break
		stack += j,
		j += 1
	return ans

def solution1(P, K):
	s = [0]*len(P)
	for i in xrange(len(P)):
		s[P[i] - 1] = i + 1
	left = 0
	right = K + 1
	res = 100000
	for i in xrange(len(s)):
		if s[i] < s[left] or s[i] <= s[right]:
			if i == right: res = min(res, max(s[left], s[right]))
			left = i
			right = K + 1 + i
	if res == 100000: return -1
	return res

def kEmptySlots(flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        f = [0]*len(flowers)
        for i in range(len(flowers)):
            f[flowers[i]-1] = i+1
        j = 0
        stack = []
        ans = -1
        while j < len(f):
            while stack:
                if j - stack[-1] - 1 == k:
                    if ans == -1 or ans > max(f[j],f[stack[-1]]):
                        ans = max(f[j],f[stack[-1]])
                if f[stack[-1]] > f[j]:
                    stack.pop()
                else:
                    break
            stack += j,
            j += 1
        return ans

print kEmptySlots([2, 4, 3, 5, 1], 2)
print solution1([2, 5, 1, 4, 3], 2)
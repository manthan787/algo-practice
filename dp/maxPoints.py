def maxPoints(elements):
    memo = [-1] * len(elements)
    return helper(elements, 0, set(), memo)

def helper(elements, i, visited, memo):
    if i >= len(elements): return 0
    if elements[i] + 1 in visited or elements[i] - 1 in visited:
        return helper(elements, i + 1, visited, memo)
    if memo[i] != -1: return memo[i]
    visited_with_delete = visited.copy()
    visited_with_delete.add(elements[i])
    del_current = elements[i] + helper(elements, i + 1, visited_with_delete, memo)
    without_del_current = helper(elements, i + 1, visited, memo)
    res = max(del_current, without_del_current)
    memo[i] = res
    return res

print maxPoints([3, 4, 2])
print maxPoints([1, 2, 1, 3, 2, 3])
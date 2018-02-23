def krakenCount(m, n):
    return krakenCountHelper(1, 1, m, n, {})

def krakenCountHelper(x, y, m, n, memo):
    a = 0
    if (x, y) in memo: return memo[(x, y)]
    if x == m and y == n: a = 1
    elif any([x > m, x < 0, y > n, y < 0]): a = 0
    else: a =  krakenCountHelper(x + 1, y, m, n, memo) \
            + krakenCountHelper(x, y + 1, m, n, memo) \
            + krakenCountHelper(x + 1, y + 1, m ,n, memo)
    memo[(x, y)] = a
    return a

print krakenCount(2, 2)
print krakenCount(3, 2)
print krakenCount(3, 3)
print krakenCount(100, 100)
def radix_sort(numbers):
    m, it = max(numbers), 0
    while 10 ** it <= m:
        buckets = [[] for _ in xrange(10)]
        for num in numbers:
            d = (num // (10 ** it)) % 10
            buckets[d].append(num)
        numbers = [num for b in buckets for num in b]
        it += 1
    return numbers


print radix_sort([10, 2, 0, 15, 1, 17, 22, 45])

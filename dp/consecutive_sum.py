def consecutive(num):
    ways = 0
    k = 1
    while(k * (k + 1) < 2 * num):
        a = (1.0 * num - (k * (k + 1) ) / 2) / (k + 1)
        if (a - int(a) == 0.0):
            ways += 1
        k += 1
    return ways

print consecutive(2)
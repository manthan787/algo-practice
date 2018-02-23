def maxPoints(elements):
    d = dict()
    for i in elements:
        d[i] = d.get(i, 0) + 1

    opt = [0] * (len(d)+1)
    keys = d.keys()
    keys.sort()

    for i in range(len(keys)):
        opt[i+1] = max([keys[i]*d[keys[i]]+opt[(i if i==0 or keys[i]>keys[i-1]+1 else i-1)], opt[i]])

    return opt[-1]


print maxPoints([3, 4, 2])
print maxPoints([1, 2, 1, 3, 2, 3])
print maxPoints([1, 1, 1, 2, 3])
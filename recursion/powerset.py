def powerset(l):
    if not l:
        return [[]]
    result = powerset(l[1:])
    return result + [subset + [l[0]] for subset in result]

print powerset(['a', 'b'])
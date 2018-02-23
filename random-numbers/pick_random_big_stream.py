'''
Uniformly picking a random element from a gigantic stream

Note: Gigantic stream. So can't keep it in memory.
'''
import random


def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        elif random.randint(1, i + 1) == 1:
            random_element = e
    return random_element

for i in xrange(4):
	print pick(xrange(1, 20))
'''
https://www.interviewcake.com/question/python/shuffle

Write a function for doing an in-place shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list
must have the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a
random integer that is >= floor and <= ceiling.
'''
import random

def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

def shuffle(l):
    ''' Go through each element call get_random
        and swap elements
    '''
    for i in xrange(len(l)):
        rand_idx = get_random(i, len(l) - 1)

        if rand_idx != i:
            l[i], l[rand_idx] = l[rand_idx], l[i]
    return l

print shuffle([1, 2, 3, 4, 5])
'''
Given a country and its population, pick a random number that chooses a country,
keeping the population in consideration. (More population, higher chances)
'''
from random import uniform

def generate(countries, populations):
    """
    Solution Explanation:

    Imagine a horizontal line for the given distribution of country populations.
    Country Population
        A     3
        B     3
        C     1
    The length of the line is sum(populations) = 7    
      A   B  C
    |###|###|#|
    1         7
    Pick a point between [1, 7]. For example, 4
    Now iterate over all populations and deduct them from
    the random number (4).
    When the random number becomes smaller than current population, 
    return that country.

    In this example, it happens when we deduct population of country A
    from random number (4 - 3) = 1, so we will return B.
    """
    rnd = uniform(1, sum(populations))

    for i, population in enumerate(populations):
        if rnd < population:
            return countries[i]
        rnd -= population
    return -1

# Test
countries = ['India', 'China', 'US', 'Canada', 'Australia']
populations = [100, 100, 78, 56, 82]

counts = {}

# Run the random number generator 1000 times.
# Since India and China have similar population, they should be selected
# almost equally. Australia should come thirds, US fourth and Canada last.
for i in xrange(1000):
    chosen_country = generate(countries, populations)
    if chosen_country in counts:
        counts[chosen_country] += 1
    else:
        counts[chosen_country] = 1

# sort countries based on number of times chosen by the weighted random generator
print sorted(counts.iteritems(), key=lambda d: d[1], reverse=True)


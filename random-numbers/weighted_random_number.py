'''
Given a country and its population, pick a random number that chooses a country,
keeping the population in consideration. (More population, higher chances)
'''
from random import uniform

def generate(countries, populations):
    total_pop = sum(populations)
    rnd = uniform(1, total_pop)

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


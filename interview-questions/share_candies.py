def solution(T):
    unique_types = set()

    # Total number of candies to be shared with
    # Mary's brother
    share = int(len(T) / 2)

    for candy_type in T:
        # If the number candy type already exists in
        # `T`, we can share this with Mary's brother
        # so decrease the `share` count
        if candy_type in unique_types:
            share -= 1
        unique_types.add(candy_type)

    # If the number of duplicates in `T` is greater than
    # N / 2, then remaining might become negative. In which
    # case, remaining is set back to 0
    if share < 0:
        share = 0
    return len(unique_types) - share


print solution([3, 4, 7, 7, 6, 6])
print solution([80, 80, 100000, 80, 80, 80, 80, 80, 80, 1235454])
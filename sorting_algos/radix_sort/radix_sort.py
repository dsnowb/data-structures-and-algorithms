def radix_sort(lst):
    """Take list of non-negative ints and return sorted list."""
    if type(lst) is not list:
        raise TypeError('argument must be type <list>')

    buckets = [[i for i in range(10)] for _ in range(10)]
    place = 1
    while len(buckets[0]) != len(lst) or place == 1:
        buckets = [[] for _ in range(10)]
        for x in lst:
            buckets[x // place % 10].append(x)
        lst = []
        for bucket in buckets:
            for x in bucket:
                lst.append(x)
        place *= 10

    return lst

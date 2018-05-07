def selection(lst):
    """Take unsorted list and return it sorted."""
    if type(lst) is not list:
        raise TypeError('argument must be of type <list>')

    for i in range(len(lst) - 1):
        mini = i
        tmp = lst[i]
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[mini]:
                mini = j
        lst[i] = lst[mini]
        lst[mini] = tmp

    return lst

def quicksort(lst):
    """Sort a list of integers."""
    if type(lst) is not list:
        raise TypeError('argument must be type <list>')
    if not len(lst):
        return lst

    ctr = 1
    for i in range(1, len(lst)):
        if lst[i] < lst[0]:
            lst[i], lst[ctr] = lst[ctr], lst[i]
            ctr += 1

    lst[0], lst[ctr - 1] = lst[ctr - 1], lst[0]
    if ctr > 2:
        lst[:ctr - 1] = quicksort(lst[:ctr - 1])
    if ctr < len(lst) - 1:
        lst[ctr:] = quicksort(lst[ctr:])
    return lst

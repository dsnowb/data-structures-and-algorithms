def mergesort(lst):
    """Take unsorted list and return it sorted."""
    if type(lst) is not list:
        raise TypeError('argument must be of type <list>')

    left = lst[:len(lst)//2]
    right = lst[len(lst)//2:]
    if len(left) > 1:
        left = mergesort(left)
    if len(right) > 1:
        right = mergesort(right)

    slst = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            slst.append(left[i])
            i += 1
        elif left[i] > right[j]:
            slst.append(right[j])
            j += 1
        else:
            slst.append(left[i])
            slst.append(right[j])
            i += 1
            j += 1

    for _ in range(i, len(left)):
        slst.append(left[_])
    for _ in range(j, len(right)):
        slst.append(right[_])

    return slst

def binary_search(arr,key):
    # validate params
    if type(arr) is not list:
        raise TypeError('arr must be type <list>')
    if type(key) is not int:
        raise TypeError('key must be type <int>')
    
    # initialize some useful variables
    max_len = len(arr) - 1
    l = 0
    r = max_len

    while l <= r and l != max_len:
        mid = (l + r + 1) // 2 if (l + r) % 2 else (l + r) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            r = mid - 1
        else:
            l = mid

    return -1

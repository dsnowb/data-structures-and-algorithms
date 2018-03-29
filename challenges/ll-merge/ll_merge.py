from ll_kth_from_end import moreBetterLL as mbll

def ll_merge(lla,llb):
    """Mutate lla into a zipped up lla and llb, consuming llb in the process"""
    # Validate arguments
    if not isinstance(lla, mbll) or not isinstance(llb, mbll):
        raise TypeError('Parameters must be linked lists')

    # Check to see if either list is empty
    if lla.head is None:
        return llb
    if llb.head is None:
        return lla

    # Initialize starting variables
    cur = lla.head
    tmp_ptr_1 = cur._next
    tmp_ptr_2 = llb.head

    # Zig-zag through lists
    while True:
        cur._next = tmp_ptr_2
        cur = cur._next
        if cur._next:
            tmp_ptr_2 = cur._next
        else:
            cur._next = tmp_ptr_1
            return lla
        cur._next = tmp_ptr_1
        cur = cur._next
        if cur._next:
            tmp_ptr_1 = cur._next
        else:
            cur._next = tmp_ptr_2
            return lla

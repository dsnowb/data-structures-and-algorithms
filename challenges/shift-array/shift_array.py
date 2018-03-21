def insertShiftArray(arr,val):
    """
    Parameters:
        arr: a list
        val: any data type
    Returns:
        an array that is arr with val inserted into the "center" index position
    """
    # Validate input
    try:
        if type(arr) != list: raise TypeError('First param not a list')
    except TypeError as err:
        print(err.args[0])
        return False
    
    # Consider edge case: empty list
    if not len(arr): return [val]

    # Insert val at mean index or mean index + .5
    new_arr = []
    for i,el in enumerate(arr):
        if i >= len(arr)/2 and i < len(arr)/2+1: new_arr.append(val)
        new_arr.append(arr[i])
    return new_arr

def improvedShiftArray(arr,val):
   # Algorithm sans exception handling
   length = len(arr) if not len(arr) % 2 else len(arr) + 1
   return arr[:length//2] + [val] + arr[length//2:]

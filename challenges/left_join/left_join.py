from .hash_table import HashTable


def left_join(htable_1, htable_2):
    """Return a left join of arguments as a dictionary of lists."""
    if type(htable_1) is not HashTable or type(htable_2) is not HashTable:
        raise TypeError('argument must be of type <HashTable>')

    res = {}
    for key in htable_1:
        res[key] = [htable_1.get(key), 'NULL']
    for key in htable_2:
        if key in res:
            res[key][1] = htable_2.get(key)

    return res

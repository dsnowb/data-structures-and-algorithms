from .linked_list import LinkedList


class HashTable:
    """Representation of a simple hash table."""
    def __init__(self, max_size=1024):
        if type(max_size) is not int:
            raise TypeError('argument must be type <int>')
        if max_size < 1:
            raise ValueError('argument must be non-negative <int>')

        self.max_size = max_size
        self.buckets = [LinkedList() for _ in range(max_size)]

    def _hash_key(self, val):
        """Return hash of val."""
        if type(val) is not str:
            raise TypeError('argument must be type <str>')

        return sum(map(lambda x: ord(x), val)) % self.max_size

    def set(self, key, val):
        """Insert key-val pair into hash table as node."""
        if type(key) is not str:
            raise TypeError('arguments must be type <str>')

        return self.buckets[self._hash_key(key)].insert({key: val})

    def get(self, key):
        """Return value stored at key."""
        if type(key) is not str:
            raise TypeError('argument must be type <str>')

        cur = self.buckets[self._hash_key(key)].head
        while cur:
            if key in cur.val.keys():
                return cur.val[key]
            cur = cur._next

    def remove(self, key, emptybuc=False):
        """Remove node storing key.

        By default, this removes the node containing key arg and returns val
        stored at node. If emptybuc arg is set to True, the bucket containing
        said node is emptied.

        """
        if type(key) is not str:
            raise TypeError('argument must be type <str>')

        buc = self.buckets[self._hash_key(key)]
        cur = buc.head
        prev = cur
        while cur:
            if key in cur.val.keys():
                if emptybuc:
                    buc.head = None
                    buc.length = 0
                else:
                    if prev is not cur:
                        prev._next = cur._next
                    else:
                        buc.head = cur._next
                return cur.val[key]

            prev = cur
            cur = cur._next

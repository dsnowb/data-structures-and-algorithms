class Node(object):
    """Define a node data type useful for a linked list"""

    def __init__(self, val, _next):
        """Instantiate node, requiring value and next pointer"""

        self.val = val
        self._next = _next

    def __str__(self):
        """Return node value"""

        return str(self.val)

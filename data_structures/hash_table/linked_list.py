from .node import Node


class LinkedList(object):
    """Define a linked list data structure"""

    def __init__(self, iterable={}):
        """Instantiate a linked list with an optional set of nodes"""

        self.head = None
        self.length = 0

        try:
            if type(iterable) is dict:
                for k, v in iterable.items():
                    self.insert({k: v})
            else:
                for i in range(len(iterable) - 1, -1, -1):
                    self.insert(iterable[i])
        except TypeError:
            print('parameter must be of type <iterable>')

    def __len__(self):
        """Return the number of nodes in linked list"""

        return self.length

    def __str__(self):
        """Return str of all node values and positions in linked list"""

        n = self.head
        s = '(HEAD) '
        while(n):
            s += '{} => '.format(n.val)
            n = n._next
        s += '(NULL)'
        return s

    def insert(self, val):
        """Add an item to the head of linked list"""

        self.head = Node(val, self.head)
        self.length += 1
        return 1

    def find(self, val):
        """Search linked list for val, return True if found else False"""

        n = self.head
        while(n):
            if n.val == val:
                return True
            n = n._next
        return False

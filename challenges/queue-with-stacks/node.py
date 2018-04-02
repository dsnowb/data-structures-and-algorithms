class Node(object):
    '''Fundamental data structure building block.

    Attributes:
        val (obj): Object being stored as data
        _next (Node) : next Node in containing data structure
   
   '''

    def __init__(self, val,_next=None):
        '''Init node value and optionally next node location'''
        self.val = val
        self._next = _next

    def __repr__(self):
        '''return node object type (node) and memory address'''
        return '<{} at {}>'.format(type(self).__name__,hex(id(self)))

    def __str__(self):
        '''Return node value as string'''
        return str(self.val)

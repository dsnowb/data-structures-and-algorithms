from node import Node

class Stack(object):
    '''Filo data structure composed of Node objects.

    Attributes:
        top: Node accessible via pop or peek.
        length: Number of nodes in the stack.

    '''

    def __init__(self, iterable = []):
        '''Initialize stack and push iterable elements into stack.'''
        self.top = None
        self.length = 0

        if type(iterable) is dict:
            for k,v in dict.items():
                self.push({k:v})

        try:
            for item in iterable:
                self.push(item)
        except TypeError:
            print('iterable must be of type <iterable>.')
    
    def __repr__(self):
        '''Return stack object.'''
        return '<{} at {}>'.format(type(self).__name__, hex(id(self)))

    def __str__(self):
        '''Return visualization of stack.'''
        s = '(TOP)'
        cur = self.top
        while cur:
            s += ' {} =>'.format(cur.val)
            cur = cur._next
        return s + ' (NULL)'

    def __len__(self):
        '''Return number of items in stack.'''
        return self.length

    def push(self,val):
        '''Add val to top of the stack.'''

        self.top = Node(val,self.top)
        self.length += 1
        return self.length

    def pop(self):
        '''Remove and return node at top of stack.'''
        if self.top:
            cur = self.top
            self.top = cur._next
            self.length -= 1
            return cur

    def peek(self):
        '''Return node at top of stack.'''
        return self.top

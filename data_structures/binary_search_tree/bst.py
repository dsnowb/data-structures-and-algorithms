class Node(object):
    '''Fundamental BST data structure building block.

    Attributes:
        val (obj): Object being stored as data
        left (Node) : left-side child Node of Node
        right (Node) : right-side child Node of Node
   
   '''

    def __init__(self, val):
        '''Init node value'''
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        '''return node object type (node) and memory address'''
        return '<{} at {}>'.format(type(self).__name__,hex(id(self)))

    def __str__(self):
        '''Return node value as string'''
        return str(self.val)


class BST(object):
    '''Binary search tree data structure.

    Attributes:
        root (Node): Highest level node, i.e. has no Node parent
    
    '''

    def __init__(self, iterable=[]):
        '''Init BST, optionally loading values in iterable'''
        
        self.root = None

        try:
            for i in iterable:
                self.insert(i)
        except:
            raise TypeError('iterable must be iterable type')

    def __repr__(self):
        return '<{} at {}>'.format(type(self), hex(id(self)))

    def __str__(self):
        s = 'Pre-ordered node values: '
        vals = []
        self.pre_order(lambda x: vals.append(str(x.val)))
        return s + ', '.join(vals) + '\b\b'

    def _walk(self, node, func, order):
        '''Traverse BST and perform func on values in passed order.'''
        '''Note: This is an internal helper function, not for public use.'''
        
        orders = {'pre_order', 'in_order', 'post_order'}
        if not (isinstance(node,Node) or callable(func) or order in orders):
            raise TypeError('Invalid _walk argument')
        
        if node is None:
            return

        if order == 'pre_order':
            func(node)

        if node.left is not None:
            try:
                self._walk(node.left, func, order)
            except RecursionError:
                print('Dept too large for current maximum recursion depth.')

        if order == 'in_order':
            func(node)

        if node.right is not None:
            try:
                self._walk(node.right, func, order)
            except RecursionError:
                print('Depth too large for current maximum recursion depth.')

        if order == 'post_order':
            func(node)

    def pre_order(self, func):
        '''Perform func on BST nodes as soon as visited'''

        if not callable(func):
            raise TypeError('func must be callable type')

        self._walk(self.root, func, 'pre_order')

    def in_order(self, func):
        '''Perform func on BST nodes in sorted order'''
        if not callable(func):
            raise TypeError('func must be callable')
        
        self._walk(self.root, func, 'in_order')

    def post_order(self, func):
        '''Perform func on BST nodes on way out of branch'''

        if not callable(func):
            raise TypeError('func must be callable')

        self._walk(self.root, func, 'post_order')

    def insert(self, val):
        '''Insert numerical val as node into BST, low values to the left'''
        if not (type(val) is int or type(val) is float):
            raise TypeError('val must be of type <int> or <float>')
        
        node = Node(val)

        if self.root is None:
            self.root = node
            return

        cur = self.root
        while True:
            if val < cur.val:
                if cur.left is None:
                    cur.left = node
                    return
                cur = cur.left

            if val >= cur.val:
                if cur.right is None:
                     cur.right = node
                     return
                cur = cur.right

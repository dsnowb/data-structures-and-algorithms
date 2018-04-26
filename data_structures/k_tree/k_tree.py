class Node:
    def __init__(self, val, children=[]):
        """Initialize with optional children values."""
        self.val = val
        self.children = []
        for child in children:
            self.children.append(Node(child))

    def __repr__(self):
        """Return string of type and address of self."""
        return '<{} at {}>'.format(type(self), hex(id(self)))

    def __str__(self):
        """Return value of node as string."""
        return str(self.val)


class KTree:
    def __init__(self, rval):
        """Initialize with root value."""
        self.root = Node(rval)

    def __repr__(self):
        """Return string of type and address of self."""
        return '<{} at {}>'.format(type(self), hex(id(self)))

    def __str__(self):
        """Return a pre-ordered listing of all nodes as a string."""
        s = []
        self.pre_order(lambda node: s.append(str(node.val)))
        return f'Pre-order: {",".join(s)}'

    def insert(self, val, pval):
        """Insert val into tree as a child node of parent with value vpal."""
        self.breadth_first_traversal(
            lambda n: n.children.append(Node(val)) if n.val == pval else False)

    def _walk(self, node, func, order):
        """Traverse tree and perform func on values in passed order."""
        """Note: This is an internal helper function, not for public use."""

        orders = {'pre_order', 'post_order'}
        if not (isinstance(node, Node) or callable(func) or order in orders):
            raise TypeError('Invalid _walk argument')

        if node is None:
            return

        if order == 'pre_order':
            func(node)

        if len(node.children):
            try:
                for child in node.children:
                    self._walk(child, func, order)
            except RecursionError:
                print('Dept too large for current maximum recursion depth.')

        if order == 'post_order':
            func(node)

    def pre_order(self, func):
        """Perform func on tree nodes as soon as visited"""

        if not callable(func):
            raise TypeError('func must be callable type')

        self._walk(self.root, func, 'pre_order')

    def post_order(self, func):
        """Perform func on tree nodes on way out of branch"""

        if not callable(func):
            raise TypeError('func must be callable')

        self._walk(self.root, func, 'post_order')

    def breadth_first_traversal(self, func):
        """Perform func on each node breadth first"""

        def recurse(nodelist):
            new_list = []
            for node in nodelist:
                func(node)
                for child in node.children:
                    new_list.append(child)

            if len(new_list):
                recurse(new_list)

        if self.root:
            recurse([self.root])

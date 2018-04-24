from bst import BST

def find_maximum_value(bst):
    '''Find the maximum balue in a tree'''

    if not isinstance(bst,BST):
        raise TypeError('argument must be of type <BST')

    if not bst.root:
        return None
        
    cur = bst.root.val

    def update(node):
        nonlocal cur
        if node.val > cur:
            cur = node.val
        
    bst.pre_order(update)
    return cur

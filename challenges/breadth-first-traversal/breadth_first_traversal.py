from bst import BST

def breadth_first_traversal(bst):
    '''Print each node in bst, breadth first'''

    if not isinstance(bst, BST):
        raise TypeError('argument must be of type <BST>')

    bfl = []

    def recurse(nodelist):
        new_list = []
        for node in nodelist:
            bfl.append(node)
            if node.left:
                new_list.append(node.left)
            if node.right:
                new_list.append(node.right)

        if len(new_list):
            recurse(new_list)

    if bst.root:
        recurse([bst.root])

    for node in bfl:
        print(node.val)

    return bfl

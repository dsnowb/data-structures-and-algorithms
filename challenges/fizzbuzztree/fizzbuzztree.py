from bst import BST

def fizz_buzz_tree(bst):
    '''Applies FizzBuzz to binary search tree'''
    if not isinstance(bst,BST):
        raise TypeError('argument must be of type <BST>')

    def fb(node):
        print(node.val)
        if not abs(node.val + 15) % 15:
            node.val = 'FizzBuzz'
            return
        if not abs(node.val + 5) % 5:
            node.val = 'Buzz'
        elif not abs(node.val + 3) % 3:
            node.val = 'Fizz'
        return

    bst.pre_order(fb)
    return bst

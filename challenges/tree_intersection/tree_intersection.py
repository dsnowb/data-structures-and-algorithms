from .bst import BST


def tree_intersection(tree_1, tree_2):
    """Returns a set containing the values shared by both input trees."""
    if type(tree_1) is not BST or type(tree_2) is not BST:
        raise TypeError('argument must be of type <BST>')

    set_1 = set()
    set_2 = set()
    tree_1.pre_order(lambda x: set_1.add(x.val))
    tree_2.pre_order(
        lambda x: set_2.add(x.val) if x.val in set_1 else False)

    return set_2

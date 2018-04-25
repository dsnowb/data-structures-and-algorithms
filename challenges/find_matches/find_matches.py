from .k_tree import KTree


def find_matches(term, tree):
    """Return nodes in tree with value of term"""
    if not isinstance(tree, KTree):
        raise TypeError('argument must be of type <KTree>')

    matches = []
    tree.pre_order(lambda n: matches.append(n) if n.val == term else False)
    return matches

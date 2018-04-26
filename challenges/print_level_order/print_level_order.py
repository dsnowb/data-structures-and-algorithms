from .k_tree import KTree


def print_level_order(tree):
    '''prints each level of k-tree on own line'''
    if not isinstance(tree, KTree):
        raise TypeError('argument must be of type <KTree>')

    all_strings = ''  # For testing output

    def recurse(nodelist):
        nonlocal all_strings
        new_list = []
        substring = ''
        for node in nodelist:
            substring += str(node.val) + ' '
            for child in node.children:
                new_list.append(child)
        
        all_strings += substring[0:-1] + '\n'

        if len(new_list):
            recurse(new_list)

    if tree.root:
        recurse([tree.root])

    return all_strings[0:-1]

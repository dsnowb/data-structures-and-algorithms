def test_node_valid_num(n_node):
    """Validate node creation with numerical value"""

    assert n_node.val == 1
    assert n_node._next is None

def test_node_valid_alpha(a_node):
    """Validate node creation with string value"""

    assert a_node.val == 'a'
    assert a_node._next is None

def test_node_print(n_node,a_node):
    """Validate printing node returns node.val"""
    
    assert n_node.__str__() == '1'
    assert a_node.__str__() == 'a'

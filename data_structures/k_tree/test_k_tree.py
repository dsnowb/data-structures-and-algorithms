import pytest
from .k_tree import Node


def test_pre_order_small(small_k_tree):
    """Validate pre ordering on small tree."""
    test_string = "0,11,12,13"
    s = []
    small_k_tree.pre_order(lambda n: s.append(str(n.val)))
    assert ",".join(s) == test_string


def test_pre_order_mid(mid_k_tree):
    """Validate pre ordering on larger tree."""
    test_string = "0,11,21,22,12,23,13,24,25,26,27,31,32"
    s = []
    mid_k_tree.pre_order(lambda n: s.append(str(n.val)))
    assert ",".join(s) == test_string


def test_post_order_small(small_k_tree):
    """Validate post ordering on small tree."""
    test_string = "11,12,13,0"
    s = []
    small_k_tree.post_order(lambda n: s.append(str(n.val)))
    assert ",".join(s) == test_string


def test_post_order_mid(mid_k_tree):
    """Validate post ordering on larger tree."""
    test_string = "21,22,11,23,12,24,25,26,31,32,27,13,0"
    s = []
    mid_k_tree.post_order(lambda n: s.append(str(n.val)))
    assert ",".join(s) == test_string


def test_breadth_first(mid_k_tree):
    """Validate breadth first ordering."""
    test_string = "0,11,12,13,21,22,23,24,25,26,27,31,32"
    s = []
    mid_k_tree.breadth_first_traversal(lambda n: s.append(str(n.val)))
    assert ",".join(s) == test_string


def test_node_repr():
    """Validate node repr."""
    node = Node(0)
    assert repr(node) == "<{} at {}>".format(type(node), hex(id(node)))


def test_tree_repr(small_k_tree):
    """Validate tree repr."""
    assert repr(small_k_tree) == \
        "<{} at {}>".format(type(small_k_tree), hex(id(small_k_tree)))


def test_node_str():
    """Validate node print string."""
    node = Node(0)
    assert str(node) == "0"


def test_tree_str(small_k_tree):
    """Validate tree print string."""
    assert str(small_k_tree) == "Pre-order: 0,11,12,13"


def test_bad_traversal_parameter(small_k_tree):
    """Pass invalid parameter to traversals."""
    with pytest.raises(TypeError):
        assert small_k_tree.pre_order(7)
        assert small_k_tree.post_order(7)
        assert small_k_tree.breadth_first_traversal(7)


def test_insertion(small_k_tree):
    """Test insertion works as expected."""
    small_k_tree.insert(21, 11)
    assert small_k_tree.root.children[0].children[0].val == 21


def test_no_insertion(small_k_tree):
    """Test insertion inserts nothing if no matching parent."""
    small_k_tree.insert(21,15)
    match = []
    small_k_tree.pre_order(lambda n: match.append(n) if n.val == 21 else False)
    assert not len(match)

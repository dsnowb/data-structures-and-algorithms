from bst import BST
import pytest
from breadth_first_traversal import breadth_first_traversal as bft

def test_invalid_input():
    '''Test invalid argument.'''
    with pytest.raises(TypeError):
        assert bft(4)

def test_assert_none():
    '''Test passing an empty bst.'''
    b = BST()
    assert not len(bft(b))

def test_single_element():
    '''Test passing a single noded bst.'''
    b = BST([1])
    assert len(bft(b)) == 1
    assert bft(b)[0].val == 1

def test_multi_element():
    '''Test a normal, unbalanced bst.'''
    b = BST([3,7,2,5,18,9,6,3,7])
    bfl = [3,2,7,5,18,3,6,9,7]
    test_bfl = bft(b)

    for i,x in enumerate(bfl):
        assert x == test_bfl[i].val

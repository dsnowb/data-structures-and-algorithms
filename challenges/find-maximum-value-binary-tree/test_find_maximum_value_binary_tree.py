import pytest
from bst import BST
from find_maximum_value_binary_tree import find_maximum_value

def test_invalid_arg():
    '''Test invalid parameter'''
    with pytest.raises(TypeError):
        find_maximum_value(4)

def test_empty_bst():
    '''Test an empty bst has no max value'''
    assert find_maximum_value(BST()) is None

def test_single_bst():
    '''Test single valued bst'''
    assert find_maximum_value(BST([1])) == 1

def test_multi_bst():
    '''Test multi-valued non-balanced bst'''
    l = [5,2,15,33,1,8,7,4,2,66,5,1,0,-2]
    b = BST(l)
    assert find_maximum_value(b) == 66

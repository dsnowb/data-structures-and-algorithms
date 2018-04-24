import pytest
from .print_level_order import print_level_order as plo


def test_invalid_argument():
    '''Test passing invalid argument to function.'''
    with pytest.raises(TypeError):
        assert plo(4)


def test_small_tree(small_k_tree):
    '''Test small, uniform k-tree.'''
    expected = ['0', '11 12 13']
    assert '\n'.join(expected) == plo(small_k_tree)


def test_mid_tree(mid_k_tree):
    '''Test mid-sized, irregular k-tree.'''
    expected = ['0', '11 12 13', '21 22 23 24 25 26 27', '31 32']
    assert '\n'.join(expected) == plo(mid_k_tree)

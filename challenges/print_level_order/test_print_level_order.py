import pytest
from .print_level_order import print_level_order as plo


def test_invalid_argument():
    '''Test passing invalid argument to function.'''
    with pytest.raises(TypeError):
        assert plo(4)


def test_small_tree(small_k_tree):
    '''Test small, uniform k-tree.'''
    expected = ['0', '11 12 13']
    result = plo(small_k_tree)

    for i, string in enumerate(result):
        assert string == expected[i]


def test_mid_tree(mid_k_tree):
    '''Test mid-sized, irregular k-tree.'''
    expected = ['0', '11 12 13', '21 22 23 24 25 26 27', '31 32']
    result = plo(mid_k_tree)

    for i, string in enumerate(result):
        assert string == expected[i]

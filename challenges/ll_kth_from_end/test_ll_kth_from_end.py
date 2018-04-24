from ll_kth_from_end import *
import pytest as pt

l = moreBetterLL([1,2,3,4,5,6])

def test_k_value_alpha():
    """Validate exception raised when non-int passed"""
    with pt.raises(TypeError):
        assert l.kthFromEnd('a')

def test_k_value_valid():
    """Validate returns correct node when valid value passed"""
    assert l.kthFromEnd(0).val == 6
    assert l.kthFromEnd(5).val == 1

def test_k_value_oor():
    """Validate exception raised when invalid (out of range) int passed"""
    with pt.raises(IndexError):
        assert l.kthFromEnd(-1)
        assert l.kthFromEnd(6)

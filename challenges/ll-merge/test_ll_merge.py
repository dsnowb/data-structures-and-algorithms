from ll_kth_from_end import moreBetterLL as mbll
from ll_merge import *
import pytest as pt

def test_invalid_params():
    """Validate inputs are mbll objects."""
    with pt.raises(TypeError):
        assert ll_merge('a', mbll([]))
        assert ll_merge(mbll([]), 'b')

def test_empty_lls():
    """Validate works propertly with two empty linked lists."""
    assert ll_merge(mbll([]),mbll([])).__str__() == '(HEAD) (NULL)'
    
def test_one_empty_ll():
    """Validate works properly when one arg is empty ll and the other has elements."""
    assert ll_merge(mbll([]),mbll([1])).__str__() == '(HEAD) 1 => (NULL)'
    assert ll_merge(mbll([1]),mbll([])).__str__() == '(HEAD) 1 => (NULL)'

def test_equal_size_ll():
    """Validate works properly when linked lists are of equal length"""
    assert ll_merge(mbll([1,2,3]),mbll([4,5,6])).__str__() == '(HEAD) 1 => 4 => 2 => 5 => 3 => 6 => (NULL)'
    assert ll_merge(mbll([1]),mbll([2])).__str__() == '(HEAD) 1 => 2 => (NULL)'

def test_unequal_size_ll():
    """Validate works properly when one linked list is larger than the other"""
    assert ll_merge(mbll([1,2]),mbll([3,4,5,6])).__str__() == '(HEAD) 1 => 3 => 2 => 4 => 5 => 6 => (NULL)'
    assert ll_merge(mbll([1,2,3,4]),mbll([5,6])).__str__() == '(HEAD) 1 => 5 => 2 => 6 => 3 => 4 => (NULL)'

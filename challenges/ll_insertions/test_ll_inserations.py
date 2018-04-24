from ll_insertions import *

def test_append_empty():
    """Tests appending to empty ll"""
    bll = betterLL([])
    assert bll.append(4).__str__() == '(HEAD) 4 => (NULL)'

def test_append_full():
    """Tests appending to ll with existing elements"""
    bll = betterLL([1,2,3])
    assert bll.append(4).__str__() == '(HEAD) 1 => 2 => 3 => 4 => (NULL)'

def test_insertBefore_empty():
    """Tests insertBefore on an empty ll"""
    bll = betterLL([])
    assert bll.insertBefore(4,'cat') == 'Specified value not found.'

def test_insertBefore_in():
    """Tests insertBefore passing a value that exists in the ll"""
    bll = betterLL([1,2,3])
    assert bll.insertBefore(3,'cat').__str__() == '(HEAD) 1 => 2 => cat => 3 => (NULL)'

def test_insertBefore_not_in():
    """Tests insertAfter passing a value that does not exist in ll"""
    bll = betterLL([1,2,3])
    assert bll.insertBefore(4,'cat') == 'Specified value not found.'

def test_insertAfter_empty():
    """Tests insertAfter on an empty ll"""
    bll = betterLL([])
    assert bll.insertAfter(4,'cat') == 'Specified value not found.'

def test_insertAfter_in():
    """Tests insertAfter passing a value that exists in the ll"""
    bll = betterLL([1,2,3])
    assert bll.insertAfter(3,'cat').__str__() == '(HEAD) 1 => 2 => 3 => cat => (NULL)'

def test_insertAfter_not_in():
    """Tests insertAfter passing a value that does not exist in the ll"""
    bll = betterLL([1,2,3])
    assert bll.insertAfter(4,'cat') == 'Specified value not found.'


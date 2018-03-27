from ll_insertions import *

def test_append_empty():
    bll = betterLL([])
    assert bll.append(4).__str__() == '(HEAD) 4 => (NULL)'

def test_append_full():
    bll = betterLL([1,2,3])
    assert bll.append(4).__str__() == '(HEAD) 1 => 2 => 3 => 4 => (NULL)'

def test_insertBefore_empty():
    bll = betterLL([])
    assert bll.insertBefore(4,'cat') == 'Specified value not found.'

def test_insertBefore_in():
    bll = betterLL([1,2,3])
    assert bll.insertBefore(3,'cat').__str__() == '(HEAD) 1 => 2 => cat => 3 => (NULL)'

def test_insertBefore_not_in():
    bll = betterLL([1,2,3])
    assert bll.insertBefore(4,'cat') == 'Specified value not found.'

def test_insertAfter_empty():
    bll = betterLL([])
    assert bll.insertAfter(4,'cat') == 'Specified value not found.'

def test_insertAfter_in():
    bll = betterLL([1,2,3])
    assert bll.insertAfter(3,'cat').__str__() == '(HEAD) 1 => 2 => 3 => cat => (NULL)'

def test_insertAfter_not_in():
    bll = betterLL([1,2,3])
    assert bll.insertAfter(4,'cat') == 'Specified value not found.'


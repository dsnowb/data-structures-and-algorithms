from pytest import raises
from .selection import selection as ss
from random import random, randint


def test_invalid_parass():
    """Validate incorrect param raises."""
    with raises(TypeError):
        ss('a')


def test_empty_list():
    """Validate empty list returns empty list."""
    assert ss([]) == []


def test_single_list():
    """Validate list with single element returns single element."""
    assert ss([1]) == [1]


def test_in_order_list():
    """Validate list already in order returns in order."""
    assert ss([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_odd_list():
    """Validate list of odd number of elements sorts."""
    assert ss([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]


def test_duplicates():
    """Validate that duplicates are retained."""
    assert ss([3, 3, 2, 2, 5]) == [2, 2, 3, 3, 5]


def test_even_list():
    """Validate that an even number of elements sorts."""
    assert ss([5, 2, 8, 15, 2, 16]) == [2, 2, 5, 8, 15, 16]


def test_random_lists():
    """Validate random lists."""
    for _ in range(10):
        lst = [random() for i in range(0, randint(10, 100))]
        slst = ss(lst)
        for i in range(len(slst) - 1):
            assert slst[i] <= slst[i + 1]

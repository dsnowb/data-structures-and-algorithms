from bst import BST
import pytest
from random import randint

@pytest.fixture
def empty_bst():
    '''Empty BST'''

    return BST()


@pytest.fixture
def small_bst():
    '''BST with a few elements'''

    return BST([1,2,3])

@pytest.fixture
def med_bst():
    '''BST with a few elements'''

    return BST([4,1,6,3,2,5,7])

@pytest.fixture
def rand_bst():
    '''Random BST with 100 elements'''

    return BST([randint(1,100) for i in range(100)])

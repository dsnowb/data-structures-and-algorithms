from .stack import Stack
import pytest

@pytest.fixture
def empty_stack():
    '''Instantiate stack with no nodes'''
    return Stack()

@pytest.fixture
def single_item_stack():
    '''Instantiate stack with single node'''
    return Stack([1])

@pytest.fixture
def iter_stack():
    '''Instantiate stack with multiple nodes'''
    return Stack(['a',1,'b',2])

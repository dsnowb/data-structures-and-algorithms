from .queue import Queue
import pytest

@pytest.fixture
def empty_queue():
    '''Instantiate queue with no nodes'''
    return Queue()

@pytest.fixture
def single_item_queue():
    '''Instantiate queue with single node'''
    return Queue([1])

@pytest.fixture
def iter_queue():
    '''Instantiate queue with multiple nodes'''
    return Queue(['a',1,'b',2])

import pytest
from node import Node
from linked_list import LinkedList as LL

@pytest.fixture
def n_node():
    return Node(1,None)

@pytest.fixture
def a_node():
    return Node('a',None)

@pytest.fixture
def empty_linked_list():
    return LL()

@pytest.fixture
def n_linked_list_list():
    return LL([1,2,3])

@pytest.fixture
def m_linked_list_list():
    return LL([1,'b',2,'d'])

@pytest.fixture
def linked_list_dict():
    return LL({'a':1,'b':2,'c':3})

@pytest.fixture
def linked_list_tuple():
    return LL((1,2,3))

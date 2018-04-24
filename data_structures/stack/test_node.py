from .node import Node
import pytest


def test_create_node():
    '''Validate that val is assigned properly on init.'''
    assert Node('a').val == 'a'


def test_create_node_next():
    '''Validate _next is assigned properly on init.'''
    assert Node(1,Node('b'))._next.val == 'b'


def test_bad_params():
    '''Validate no value arg results in exception.'''
    with pytest.raises(TypeError):
        assert Node()


def test_both_params():
    '''Validate inserting two args results in proper init.'''
    n = Node('a',Node('b'))
    assert n.val == 'a'
    assert n._next.val == 'b'


def test_repr():
    '''Validate repr returns Node type and address.'''
    n = Node(1)
    assert n.__repr__() == '<Node at {}>'.format(hex(id(n)))


def test_str():
    '''Validate __str__ prints node value.'''
    n = Node(1)
    assert n.__str__() == '1'

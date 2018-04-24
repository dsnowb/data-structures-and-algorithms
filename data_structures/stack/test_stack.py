from .stack import Stack
import pytest


def test_empty_stack(empty_stack):
    '''Validate empty stack contains no nodes'''
    assert empty_stack.top is None


def test_add_to_empty_stack(empty_stack):
    '''Validate pushing to empty stack adds one node'''
    empty_stack.push('b')
    assert empty_stack.top.val == 'b'
    assert empty_stack.top._next is None


def test_add_to_full_stack(iter_stack):
    '''Validate pushing to full stack adds on top of existing nodes'''
    iter_stack.push('c')
    iter_stack.top.val == 'c'
    assert iter_stack.top._next.val == 2


def test_pop_empty_stack(empty_stack):
    '''Validate popping empty stack returns None'''
    assert empty_stack.pop() is None


def test_pop_single_stack(single_item_stack):
    '''Validate popping last node results in empty stack'''
    assert single_item_stack.pop().val is 1
    assert single_item_stack.pop() is None


def test_pop_iter_stack(iter_stack):
    '''Validate popping full stack returns expected order'''
    l = [2, 'b', 1, 'a']
    for i in range(len(l)):
        assert iter_stack.pop().val == l[i]
    assert iter_stack.pop() is None


def test_peek(iter_stack):
    '''Validate that peek returns expected node and does not mutate stack'''
    assert iter_stack.peek().val == 2
    assert iter_stack.top.val == 2


def test_rest_length(empty_stack, iter_stack):
    '''Validate length has expected values'''
    assert len(empty_stack) == 0
    assert len(iter_stack) == 4


def test_push_pop_length(empty_stack):
    '''Validate length after pushing and popping'''
    empty_stack.push(1)
    assert len(empty_stack) == 1
    empty_stack.pop()
    assert len(empty_stack) == 0


def test_invalid_iterable():
    '''Validate passing non-iterable argument raises exception'''
    with pytest.raises(Exception):
        assert Stack(4)


def test_repr(empty_stack):
    assert empty_stack.__repr__() == '<Stack at {}>'.format(hex(id(empty_stack)))


def test_str(iter_stack):
    assert iter_stack.__str__() == '(TOP) 2 => b => 1 => a => (NULL)' 

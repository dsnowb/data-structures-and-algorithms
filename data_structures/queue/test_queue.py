from .queue import Queue
import pytest


def test_empty_queue(empty_queue):
    '''Validate empty queue contains no nodes'''
    assert empty_queue.front is None
    assert empty_queue.back is None


def test_add_to_empty_queue_front(empty_queue):
    '''Validate enqueuing to empty queue adds one node and is front'''
    empty_queue.enqueue('b')
    assert empty_queue.front.val == 'b'
    assert empty_queue.front._next is None


def test_add_to_empty_queue_back(empty_queue):
    '''Validate enqueuing to empty queue adds one node and is back'''
    empty_queue.enqueue('b')
    assert empty_queue.back.val == 'b'
    assert empty_queue.back._next is None


def test_add_to_full_queue(iter_queue):
    '''Validate enqueuing to full queue adds to back of queue'''
    iter_queue.enqueue('c')
    assert iter_queue.back.val == 'c'
    assert iter_queue.front.val == 'a'


def test_dequeue_empty_queue(empty_queue):
    '''Validate dequeueing empty queue returns None'''
    assert empty_queue.dequeue() is None


def test_dequeue_single_queue(single_item_queue):
    '''Validate dequeueing last node results in empty queue'''
    assert single_item_queue.dequeue().val is 1
    assert single_item_queue.dequeue() is None


def test_dequeue_iter_queue(iter_queue):
    '''Validate dequeueping full queue returns expected order'''
    l = ['a', 1, 'b', 2]
    for i in range(len(l)):
        assert iter_queue.dequeue().val == l[i]
    assert iter_queue.dequeue() is None


def test_rest_length(empty_queue, iter_queue):
    '''Validate length has expected values'''
    assert len(empty_queue) == 0
    assert len(iter_queue) == 4


def test_enqueue_dequeue_length(empty_queue):
    '''Validate length after enqueuing and dequeueping'''
    empty_queue.enqueue(1)
    assert len(empty_queue) == 1
    empty_queue.dequeue()
    assert len(empty_queue) == 0


def test_invalid_iterable():
    '''Validate passing non-iterable argument raises exception'''
    with pytest.raises(Exception):
        assert queue(4)


def test_repr(empty_queue):
    assert empty_queue.__repr__() == '<Queue at {}>'.format(hex(id(empty_queue)))


def test_str(iter_queue):
    assert iter_queue.__str__() == '(FRONT) a => 1 => b => 2 (BACK)' 

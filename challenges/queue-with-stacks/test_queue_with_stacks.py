from queue_with_stacks import Queue as Q
import pytest

def test_enqueue_return():
    '''Validate return value of enqueue.'''

    assert Q().enqueue(2) == 2

def test_enqueue_one_item_queue():
    '''Validate enqueue properly enqueues item.'''

    q = Q()
    q.enqueue(2)
    assert q.dequeue().val == 2

def test_enqueue_list():
    '''Validate enqueue properly enqueues other data types.'''

    q = Q()
    q.enqueue([1,2,3,4,5])
    assert q.dequeue().val[2] == 3

def test_dequeue_empty():
    '''Validate dequeuing an empty queue returns None.'''

    assert Q().dequeue() is None

def test_dequeue_one():
    '''Validate that dequeuing one item returns item, then returns.'''

    q = Q()
    q.enqueue(1)
    assert q.dequeue().val == 1
    assert q.dequeue() is None

def test_dequeue_multi():
    '''Validate that dequeuing multiple items.'''

    q = Q()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue().val == 1
    assert q.dequeue().val == 2

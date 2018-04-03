from fifo_animal_shelter import AnimalShelter as AS
import pytest

@pytest.fixture
def empty_as():
    '''produce empty AnimalShelter'''
    return AS()

@pytest.fixture
def single_as():
    '''produce AnimalShelter with one node'''
    a = AS()
    a.enqueue('cat')
    return a

@pytest.fixture
def full_as():
    '''produce full AnimalShelter'''
    a = AS()
    a.enqueue('cat')
    a.enqueue('dog')
    a.enqueue('cat')
    return a

def test_enqueue_invalid(empty_as):
    '''Expect invalid arg raises exception'''
    with pytest.raises(TypeError):
        assert empty_as.enqueue('frog')

def test_enqueue_valid(empty_as):
    '''Expect correct arg enqueues'''
    assert empty_as.enqueue('cat') == 'cat'
    assert empty_as.enqueue('dog') == 'dog'

def test_enqueue_order(full_as):
    '''Expect enqueue to queue correct fifo order'''
    assert full_as.front.val == 'cat'
    assert full_as.front._next.val == 'dog'

def test_dequeue_empty_valid(empty_as):
    '''Expect dequeue empty_as with valid argument returns None'''
    assert empty_as.dequeue('dog') is None

def test_dequeue_empty_invalid(empty_as):
    '''Expect dequeue invalid argument raises exception'''
    with pytest.raises(TypeError):
        assert empty_as.dequeue('frog')

def test_dequeue_one(single_as):
    '''Expect dequeue to dequeue one then None'''
    assert single_as.dequeue().val == 'cat'
    assert single_as.dequeue() is None

def test_dequeue_dog(full_as):
    '''Expect one dog in full_as'''
    assert full_as.dequeue('dog').val == 'dog'
    assert full_as.dequeue('dog') is None

def test_dequeue_cat(full_as):
    '''Expect two cats in full_as'''
    assert full_as.dequeue('cat').val == 'cat'
    assert full_as.dequeue('cat').val == 'cat'

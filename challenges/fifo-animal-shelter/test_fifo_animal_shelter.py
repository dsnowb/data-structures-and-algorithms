from fifo_animal_shelter import Dog, Cat, AnimalShelter as AS
import pytest

@pytest.fixture
def empty_as():
    '''produce empty AnimalShelter'''
    return AS()

@pytest.fixture
def single_as():
    '''produce AnimalShelter with one node'''
    a = AS()
    a.enqueue(Cat())
    return a

@pytest.fixture
def full_as():
    '''produce full AnimalShelter'''
    a = AS()
    a.enqueue(Cat())
    a.enqueue(Dog())
    a.enqueue(Cat())
    return a

def test_enqueue_invalid(empty_as):
    '''Expect invalid arg raises exception'''
    with pytest.raises(TypeError):
        assert empty_as.enqueue('frog')

def test_enqueue_valid(empty_as):
    '''Expect correct arg enqueues'''
    assert isinstance(empty_as.enqueue(Cat()), Cat)
    assert isinstance(empty_as.enqueue(Dog()), Dog)

def test_enqueue_order(full_as):
    '''Expect enqueue to queue correct fifo order'''
    assert isinstance(full_as.front.val, Cat)
    assert isinstance(full_as.front._next.val, Dog)

def test_dequeue_empty_valid(empty_as):
    '''Expect dequeue empty_as with valid argument returns None'''
    assert empty_as.dequeue(Dog()) is None

def test_dequeue_empty_invalid(empty_as):
    '''Expect dequeue invalid argument raises exception'''
    with pytest.raises(TypeError):
        assert empty_as.dequeue('frog')

def test_dequeue_one(single_as):
    '''Expect dequeue to dequeue one then None'''
    assert isinstance(single_as.dequeue().val, Cat)
    assert single_as.dequeue() is None

def test_dequeue_dog(full_as):
    '''Expect one dog in full_as'''
    assert isinstance(full_as.dequeue(Dog()).val, Dog)
    assert full_as.dequeue(Dog()) is None

def test_dequeue_cat(full_as):
    '''Expect two cats in full_as'''
    assert isinstance(full_as.dequeue(Cat()).val, Cat)
    assert isinstance(full_as.dequeue(Cat()).val, Cat)

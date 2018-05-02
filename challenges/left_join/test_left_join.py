from pytest import raises, fixture
from random import randint
from .hash_table import HashTable as HT
from .left_join import left_join as lj


@fixture
def random_hash_table():
    """Yield a hash table with random key:value pairs."""
    htable = HT()
    for _ in range(randint(1, 100)):
        htable.set(str(randint(1, 100**10)), str(randint(1, 100**10)))
    yield htable


def test_invalid_arguments():
    """Validate passing wrong type raises."""
    with raises(TypeError):
        assert lj(2, HT())
        assert lj(HT(), 'a')


def test_empty_left(random_hash_table):
    """Validate passing an empty left table returns empty."""
    assert not len(lj(HT(), HT()))
    assert not len(lj(HT(), random_hash_table))


def test_empty_right(random_hash_table):
    """Validate empty right returns only left values."""
    res = lj(random_hash_table, HT())
    for key in random_hash_table:
        assert random_hash_table.get(key) == res[key][0]
    for key in res:
        assert res[key] == [random_hash_table.get(key), 'NULL']


def test_left_join_valid():
    """Validate left join function returns expected values."""
    htable_1, htable_2 = HT(), HT()
    htable_1.set('a', 1)
    htable_1.set('b', 2)
    htable_2.set('a', 3)
    htable_2.set('c', 4)

    assert lj(htable_1, htable_2) == {'a': [1, 3], 'b': [2, 'NULL']}
    assert lj(htable_2, htable_1) == {'a': [3, 1], 'c': [4, 'NULL']}

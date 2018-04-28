from .hash_table import HashTable
from pytest import fixture


@fixture
def htable():
    """Empty hash table."""
    return HashTable()


@fixture
def htable_onebuc():
    """Single bucket hash table."""
    return HashTable(1)

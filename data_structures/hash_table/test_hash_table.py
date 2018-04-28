from pytest import raises
from .hash_table import HashTable
from .linked_list import LinkedList


def test_hash_table_instantiation_invalid_arg():
    """Test invalid max_size arg raises."""
    with raises(TypeError):
        HashTable('a')


def test_hash_table_instantiation_min_size():
    """Test instantiation with non-positive int raises."""
    with raises(ValueError):
        HashTable(-1)


def test_hash_table_instantiation():
    """Test hash table instantiation with passed max_size."""
    ht = HashTable(5)
    assert len(ht.buckets) == 5
    assert isinstance(ht.buckets[0], LinkedList)
    assert ht.buckets[0].head is None


def test_hash_key_invalid_arg(htable):
    """Test non-string passed to _hash_key raises."""
    with raises(TypeError):
        htable._hash_key(4)


def test_hash_key_valid(htable):
    """Test string hashes to expected index."""
    assert htable._hash_key('abc') == 294
    assert htable._hash_key('abcdefghijklmnopqrstuvwxyz') == 799


def test_hash_key_single_valid(htable_onebuc):
    """Test strings all hash to same index in single-bucket table."""
    assert htable_onebuc._hash_key('abc') == 0
    assert htable_onebuc._hash_key('abcdefghijklmnopqustuvwxyz') == 0


def test_set_invalid_arg(htable):
    """Test setting with non-string raises."""
    with raises(TypeError):
        htable.set(1)


def test_set_key_valid(htable):
    """Test default table set results in values in correct bucket."""
    htable.set('abc', 'a')
    htable.set('abcdefghijklmnopqrstuvwxyz', 'b')
    assert htable.buckets[294].head.val['abc'] == 'a'
    assert htable.buckets[799].head.val['abcdefghijklmnopqrstuvwxyz'] == 'b'


def test_set_key_valid_single(htable_onebuc):
    """Test multiple values go into same bucket when buckets constrained."""
    htable_onebuc.set('abc', 'a')
    htable_onebuc.set('abcd', 'b')
    assert htable_onebuc.buckets[0].head.val['abcd'] == 'b'
    assert htable_onebuc.buckets[0].head._next.val['abc'] == 'a'


def test_get_invalid_arg(htable):
    """Test getting with non-string raises."""
    with raises(TypeError):
        htable.set(1)


def test_get_key_valid(htable):
    """Test able to retrieve values in different buckets."""
    htable.set('abc', 1)
    htable.set('abcd', 2)
    assert htable.get('abc') == 1
    assert htable.get('abcd') == 2


def test_get_key_valid_single(htable_onebuc):
    """Test retrieval of vals when buckets constrained."""
    htable_onebuc.set('abc', 1)
    htable_onebuc.set('abcd', 2)
    assert htable_onebuc.get('abc') == 1
    assert htable_onebuc.get('abcd') == 2


def test_remove_invalid_arg(htable):
    """Test removing with non-string raises."""
    with raises(TypeError):
        htable.set(1)


def test_remove_non_present_arg(htable_onebuc):
    """Test removing a non-present key."""
    htable_onebuc.set('abc', 1)
    htable_onebuc.remove('a')
    assert len(htable_onebuc.buckets[0]) == 1


def test_remove_valid(htable_onebuc):
    """Test removing a key."""
    htable_onebuc.set('abc', 1)
    htable_onebuc.set('abcd', 2)
    assert len(htable_onebuc.buckets[0]) == 2
    htable_onebuc.remove('abcd')
    assert htable_onebuc.get('abcd') is None
    assert htable_onebuc.get('abc') == 1


def test_remove_all(htable_onebuc):
    """Test emptying bucket."""
    htable_onebuc.set('abc', 1)
    htable_onebuc.set('abcd', 2)
    htable_onebuc.remove('abcd', True)
    assert htable_onebuc.get('abc') is None
    assert len(htable_onebuc.buckets[0]) == 0

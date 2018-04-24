import pytest

def test_insert_empty_valid(empty_bst):
    '''Test inserting into an empty bst.'''
    empty_bst.insert(3)
    assert empty_bst.root.val == 3


def test_insert_invalid(empty_bst):
    '''Test insert with invalid argument.'''

    with pytest.raises(TypeError):
        assert empty_bst.insert('a')


def test_insert_small_larger(small_bst):
    '''Test inserting larger value into proper order.'''

    small_bst.insert(5)
    assert small_bst.root.right.right.right.val == 5
    small_bst.insert(2)
    assert small_bst.root.right.right.left.val == 2


def test_insert_small_smaller(small_bst):
    '''Test inserting small value into proper order.'''
    small_bst.insert(-1)
    assert small_bst.root.left.val == -1
    small_bst.insert(0)
    assert small_bst.root.left.right.val == 0


def test_in_order_empty(empty_bst):
    '''Test performing in order function on empty bst.'''

    l = []
    empty_bst.in_order(lambda x: l.append(str(x.val)))
    assert ''.join(l) == ''


def test_pre_order_invalid(empty_bst):
    '''Test performing pre order with non-callable argument.'''
    with pytest.raises(TypeError):
        assert empty_bst.pre_order('frog')


def test_in_order_invalid(empty_bst):
    '''Test performing in order with non-callable argument.'''
    
    with pytest.raises(TypeError):
        assert empty_bst.in_order('frog')


def test_post_order_invalid(empty_bst):
    '''Test performing post order with non-callable argument.'''

    with pytest.raises(TypeError):
        assert empty_bst.post_order('frog')


def test_pre_order_small(small_bst):
    '''Test pre-ordering on small bst.'''
    
    l = []
    small_bst.pre_order(lambda x: l.append(str(x.val)))
    assert ''.join(l) == '123'


def test_post_order_small(small_bst):
    '''Test post ordering on small bst.'''

    l = []
    small_bst.post_order(lambda x: l.append(str(x.val)))
    assert ''.join(l) == '321'


def test_pre_order_med(med_bst):
    '''Test pre ordering on medium bst.'''

    l = []
    med_bst.pre_order(lambda x: l.append(str(x.val)))
    assert ''.join(l) == '4132657'


def test_in_order_med(med_bst):
    '''Test in order function with medium size bst.'''

    l = []
    med_bst.in_order(lambda x: l.append(str(x.val)))
    assert ''.join(l) == '1234567'


def test_post_order_med(med_bst):
    '''Test post order function with medium size bst.'''

    l = []
    med_bst.post_order(lambda x: l.append(str(x.val)))
    assert ''.join(l) == '2315764'


def test_in_order_rand(rand_bst):
    '''Test ordering with random values.'''

    l = []
    rand_bst.in_order(lambda x: l.append(x.val))
    for i in range(1,len(l)-1):
        assert l[i] >= l[i-1] and l[i] <= l[i+1]


def test_repr(med_bst):
    '''Test repr representation.'''

    assert med_bst.__repr__() == '<{} at {}>'.format(type(med_bst), hex(id(med_bst)))


def test_str(med_bst):
    '''Test str representation.'''

    assert med_bst.__str__() == 'Pre-ordered node values: 4, 1, 3, 2, 6, 5, 7\b\b'

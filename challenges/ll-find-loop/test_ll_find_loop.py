from ll_find_loop import smartLL as sll

def test_empty_ll():
    """Validate that empty linked list has no loop"""
    assert not sll([]).hasLoop()

def test_one_ll():
    """Validate that linked list with one element has no loop"""
    assert not sll([1]).hasLoop()

def test_multi_ll_valid():
    """Validate linked lists with multiple elements"""
    assert not sll([1,2,3,4,5]).hasLoop()
def test_multi_ll_small_loop():
    """Validate linked list with small loop"""
    s = sll([1,2,3])
    s.head._next._next._next = s.head
    assert s.hasLoop()

def test_multi_ll_large_loop():
    """Validate linked with with larger loop"""
    s = sll([1,2,3,4,5,6,7,8,9,10,11,12])
    cur = s.head
    for i in range(s.length - 1):
        cur = cur._next
    cur._next = s.head._next._next

    assert s.hasLoop()

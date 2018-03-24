def test_insert_into_empty(empty_linked_list):
    """Validate insertion into empty linked list"""

    empty_linked_list.insert(1)
    empty_linked_list.insert('b')
    assert empty_linked_list.head.val == 'b'
    assert empty_linked_list.head._next.val == 1

def test_insert_into_full_list(n_linked_list_list):
    """Validate insertion into linked list with elements"""

    n_linked_list_list.insert('z')
    assert n_linked_list_list.head.val == 'z'

def test_insert_into_full_dict(linked_list_dict):
    """
    Validate insertion into linked list built with dict
    iterable instead of list
    """

    linked_list_dict.insert('string')
    assert linked_list_dict.head.val == 'string'
    assert type(linked_list_dict.head._next.val) == dict

def test_len(n_linked_list_list):
    """Validate length of linked list with elements"""

    assert len(n_linked_list_list) == 3

def test_len_empty(empty_linked_list):
    """Validate length of empty linked list""" 

    assert len(empty_linked_list) == 0

def test_print(m_linked_list_list):
    """Validate printing linked list with elements"""

    assert m_linked_list_list.__str__() == '(HEAD) 1 => b => 2 => d => (NULL)'

def test_print_empty(empty_linked_list):
    """Validate printing empty linked list"""

    assert empty_linked_list.__str__() == '(HEAD) (NULL)'

def test_find(m_linked_list_list):
    """Validate find() in multi-typed linked list"""
    
    assert not m_linked_list_list.find(7)
    assert m_linked_list_list.find('d')

def test_find_dict(linked_list_dict):
    """Validate find() in linked list with key:value pairs"""
    
    assert linked_list_dict.find({'b':2})

def test_find_empty(empty_linked_list):
    """Validate find in empty list"""

    assert not empty_linked_list.find(1)

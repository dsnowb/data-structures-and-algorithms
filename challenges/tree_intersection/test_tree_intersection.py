from .bst import BST
from .tree_intersection import tree_intersection as ti
from pytest import raises


def test_invalid_arguments():
    """Test passing invalid arguments."""
    with raises(TypeError):
        assert ti(3, BST())
        assert ti(BST(), 4)


def test_no_overlapping_values():
    """Test passing two BST's with no overlap."""
    assert ti(BST([1, 2, 3, 4]), BST([5, 6, 7, 8])) == set()


def test_valid_values():
    """Test overlapping BST's."""
    assert ti(BST([1, 2, 3, 4]), BST([1, 2, 3, 4])) == {1, 2, 3, 4}
    assert ti(
        BST([17, 4, 8, 8, 9, 3, 2, 19]),
        BST([19, 8, 7, 17, 2, 0])
        ) == {19, 2, 17, 8}

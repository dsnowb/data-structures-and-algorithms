import pytest
from .find_matches import find_matches as fm


def test_invalid_param():
    """Test invalid param passed."""
    with pytest.raises(TypeError):
        fm(4, 4)


def test_nothing_found(mid_k_tree):
    """Test value not in tree."""
    assert len(fm(100, mid_k_tree)) == 0

def test_one_found(mid_k_tree):
    """Test single found."""
    assert len(fm(0, mid_k_tree)) == 1

def test_multi_found(mid_k_tree):
    """Test multiples found."""
    assert len(fm(22, mid_k_tree)) == 4

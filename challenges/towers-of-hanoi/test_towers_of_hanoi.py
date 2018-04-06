from towers_of_hanoi import towers_of_hanoi as toh
import pytest

def test_three():
    assert toh(3) == ['Move Disc #0', 'Move Disc #1', 'Move Disc #0', 'Move Disc #2', 'Move Disc #0', 'Move Disc #1', 'Move Disc #0']

def test_four():
    assert toh(4) == ['Move Disc #0', 'Move Disc #1', 'Move Disc #0', 'Move Disc #2', 'Move Disc #0', 'Move Disc #1', 'Move Disc #0', 'Move Disc #3', 'Move Disc #0', 'Move Disc #1', 'Move Disc #0', 'Move Disc #2', 'Move Disc #0', 'Move Disc #1', 'Move Disc #0']

def test_invalid():
    with pytest.raises(TypeError):
        assert toh('a')

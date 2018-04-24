from towers_of_hanoi import towers_of_hanoi as toh
import pytest

def test_three():
    '''Test moves for 3 discs'''
    assert toh(3) == ['Move Disc #0', 'Move Disc #1', 'Move Disc #0', 'Move Disc #2', 'Move Disc #0', 'Move Disc #1', 'Move Disc #0']

def test_four():
    '''Test moves for 4 discs'''
    assert toh(4) == ['Move Disc #0', 'Move Disc #1', 'Move Disc #0', 'Move Disc #2', 'Move Disc #0', 'Move Disc #1', 'Move Disc #0', 'Move Disc #3', 'Move Disc #0', 'Move Disc #1', 'Move Disc #0', 'Move Disc #2', 'Move Disc #0', 'Move Disc #1', 'Move Disc #0']

def test_invalid():
    '''Test invalid input'''
    with pytest.raises(TypeError):
        assert toh('a')

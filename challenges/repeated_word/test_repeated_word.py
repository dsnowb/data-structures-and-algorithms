from .repeated_word import repeated_word as rw
from pytest import raises


def test_invalid_argument():
    """Test passing non-string."""
    with raises(TypeError):
        rw(4)


def test_empty_string():
    """Test empty string returns None."""
    assert rw('') is None


def test_valid_repeat():
    """Test string with repeated words returns first repeated word."""
    assert rw('The cat in the hat.') == 'the'
    assert rw('She sells sea shells by the sea shore.') == 'sea'


def test_valid_punctuation():
    """Test function works including punctation."""
    assert rw('What did they say? Say what again!') == 'say'
    assert rw('I am... that am!') == 'am'


def test_contractions():
    """Test contractions are detected and returned as expected."""
    assert rw("Don't do things that I said don't do!") == "don't"
    assert rw("You should've heard. \"Should've\" is the word.") == "should've"

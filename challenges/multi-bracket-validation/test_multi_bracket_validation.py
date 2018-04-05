from multi_bracket_validation import multi_bracket_validation as mbv
import pytest

def test_empty():
    '''Test empty string'''
    assert mbv('')

def test_non_valid_arg():
    '''Test invalid argument'''
    with pytest.raises(TypeError):
        assert mbv(1)

def test_invalid_singles():
    '''Test invalids as singles'''
    assert not mbv('(')
    assert not mbv(')')

def test_pair_valid():
    '''Test easy pairs'''
    assert mbv('()')
    assert mbv('[]')

def test_multi_valid():
    '''Test more complex pairings'''
    assert mbv('{[]}')
    assert mbv('{a([([akdkldf])])}')

def test_pair_invalid():
    '''test basic invalids'''
    assert not mbv('{(')
    assert not mbv('[)')

def test_multi_invalid():
    '''test more complex invalids'''
    assert not mbv('{{{akdkd}}dkkd{}')
    assert not mbv('()(){})')

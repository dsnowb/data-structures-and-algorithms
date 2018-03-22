from binary_search import *
import pytest as pt

def test_binary_search_valid_params():
    with pt.raises(TypeError):
        assert binary_search('a',1)
        assert binary_search('[]','a')

def test_binary_search_key_out_of_range():
    assert binary_search([1,2],0) == -1
    assert binary_search([1,2],3) == -1

def test_binary_search_key_edge():
    assert binary_search([1,2,3,4,5,6,7,8,9], 1) == 0
    assert binary_search([1,2,3,4,5,6,7,8,9], 9) == 8

def test_binary_search_key_in_odd_arr():
    assert binary_search([1,2,3,4,5,6,7,8,9], 8) == 7
    assert binary_search([1,2,3,4,5,6,7,8,9], 3) == 2

def test_binary_search_key_in_even_arr():
    assert binary_search([1,2,3,4,5,6,7,8,9,10], 5) == 4
    assert binary_search([1,2,3,4,5,6,7,8,9,10], 7) == 6

def test_binary_search_non_consecutive():
    assert binary_search([13,34,37,64,72,99],72) == 4

def test_binary_search_empty():
    assert binary_search([],1) == -1

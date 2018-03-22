from binary_search import *
import pytest as pt

def test_binary_search_valid_params():
    '''
    tests that the params are of a valid type
    NOTE: arr elements are not validated as ints, nor is arr validated as sorted
          as this would be expensive and defeat the purpose of the binary search      
    '''
    with pt.raises(TypeError):
        assert binary_search('a',1)
        assert binary_search('[]','a')

def test_binary_search_key_out_of_range():
    '''
    tests values that do not exist in arr, both too low and too high
    '''
    assert binary_search([1,2],0) == -1
    assert binary_search([1,2],3) == -1

def test_binary_search_key_edge():
    '''
    tests array indices 0 and -1
    '''
    assert binary_search([1,2,3,4,5,6,7,8,9], 1) == 0
    assert binary_search([1,2,3,4,5,6,7,8,9], 9) == 8

def test_binary_search_key_in_odd_arr():
    '''
    tests search in an array of an odd number of elements
    '''
    assert binary_search([1,2,3,4,5,6,7,8,9], 8) == 7
    assert binary_search([1,2,3,4,5,6,7,8,9], 3) == 2

def test_binary_search_key_in_even_arr():
    '''
    tests serach in an array of an even number of elements
    '''
    assert binary_search([1,2,3,4,5,6,7,8,9,10], 5) == 4
    assert binary_search([1,2,3,4,5,6,7,8,9,10], 7) == 6

def test_binary_search_non_consecutive():
    '''
    tests array that contains more random, non-consecutive but sorted numbers
    '''
    assert binary_search([13,34,37,64,72,99],72) == 4

def test_binary_search_empty():
    '''
    tests the case of an empty array
    '''
    assert binary_search([],1) == -1

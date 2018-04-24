from largest_product import *
import pytest as pt

def test_params_valid():
    '''Validates that parameter is type list'''
    with pt.raises(TypeError):
        assert largest_product('the')

def test_one_row_eval():
    '''Validates that 1 x n matrices invalid'''
    with pt.raises(ValueError):
        assert largest_product([[3],[4]])

def test_one_col_eval():
    '''Validates that m x 1 matrices invalid'''
    with pt.raises(ValueError):
        assert largest_product([[3,4]])

def test_min_matrix_eval():
    '''Validates that a 2x2 matrix returns expected value'''
    assert largest_product([[4,6],[7,2]]) == 42

def test_matrix_eval():
    '''Validates m x n matrices return correct values'''
    assert largest_product([[1,2,7,9],[4,9,6,8],[3,2,3,1]]) == 72
    assert largest_product([[1,2],[7,4],[2,12],[3,1]]) == 84

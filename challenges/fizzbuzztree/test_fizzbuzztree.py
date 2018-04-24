from fizzbuzztree import fizz_buzz_tree as fbt
from bst import BST
import pytest

def test_invalid_input():
    '''Test invalid input raises exception.'''
    with pytest.raises(TypeError):
        assert fbt(3)

def test_no_fizzbuzz():
    '''Test a tree without any fizzbuzz elements'''
    l = [1,2,7,13,8]
    b = BST(l)

    l_after = []
    fbt(b).pre_order(lambda x: l_after.append(x.val))
    for i,x in enumerate(l):
        assert x == l_after[i]

def test_fizzbuzz():
    '''Test a tree with fizzbuzz elements'''
    l = [i for i in range(20)]
    b = BST(l)

    l_fb = ['FizzBuzz',1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz',11,'Fizz',\
            13,14,'FizzBuzz',16,17,'Fizz',19]
    l_after = []
    fbt(b).pre_order(lambda x: l_after.append(x.val))
    for i,x in enumerate(l_fb):
        print(x)
        print(l_after[i])
        assert x == l_after[i]

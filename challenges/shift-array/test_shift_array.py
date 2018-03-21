from shift_array import *

def test_inputs(): assert insertShiftArray(5,2) == False

def test_empty_array(): assert insertShiftArray([],1) == [1]

def test_insert_middle(): assert insertShiftArray([1,2],'a') == [1,'a',2]

def test_insert_middle_odd(): assert insertShiftArray([1,2,3], 'a') == [1,2,'a',3]

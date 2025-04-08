from lib.high_value import *

def test_value_first_checker():
    highvalue = HighValue(10, 4)
    assert highvalue.value_first == 10
    # checked that first value passes and fails correctly
    
def test_value_second_checker():
    highvalue = HighValue(10, 4)
    assert highvalue.value_second == 4
    # checked that second value passes and fails correctly

def test_first_get_highest():
    highvalue = HighValue(10, 4)
    assert highvalue.get_highest() == "First value is higher"

def test_second_get_highest():
    highvalue = HighValue(10, 14)
    assert highvalue.get_highest() == "Second value is higher"

def test_equal_get_highest():
    highvalue = HighValue(10, 10)
    assert highvalue.get_highest() == "Values are equal"

def test_add_first():
    highvalue = HighValue(10, 4)
    highvalue.add(7, "first")
    assert highvalue.value_first == 17

def test_add_second():
    highvalue = HighValue(10, 4)
    highvalue.add(10, "second")
    assert highvalue.value_second == 14

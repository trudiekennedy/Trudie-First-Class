from lib.high_value import *

def test_value_first_checker():
    highvalue = HighValue(10, 4)
    assert highvalue.value_first == 10
    # checked that first value passes and fails correctly
    
def test_value_second_checker():
    highvalue = HighValue(10, 4)
    assert highvalue.value_second == 4
    # checked that second value passes and fails correctly


# check values are actually integers
# check values are assigned to self
# test if values are not integers
# test if values are integers
# test if values are present


# test get_highest
# testing scenario where first is higher
# where second is higher
# where both are equal

# assert that first == number
# assert that second == number
# check that first/second + increase == correct
# check if variables are not inputted

# check get_highest again with new values
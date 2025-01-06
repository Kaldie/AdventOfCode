from pytest import fixture
from solve_1 import * 
@fixture
def input_too_manny():
   return "????.?.#.? 1,1,1"

def test_simple():
    assert calculate_number_of_options("????",1) == 4
    assert calculate_number_of_options("????",2) == 3
    assert calculate_number_of_options("????",3) == 2
    assert calculate_number_of_options("????",4) == 1

def test_for_too_many(input_too_manny):
    assert solve_line(input_too_manny) == (2*4)+(3)

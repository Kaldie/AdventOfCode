from pytest import fixture
from solve import solve, get_number_of_mem_blocks
from solve2 import solve as solve2


@fixture
def input():
    return ["2333133121414131402"]

def test_num_of_blocks(input):
    assert get_number_of_mem_blocks(input[0]) == 9

def test_solve(input):
    x =solve(input)
    assert x==1928

def test_solve2(input):
    x =solve2(input)
    assert x == 2858
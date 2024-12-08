from pytest import fixture
from solve import find_start, solve
from solve2 import solve as solve2
@fixture
def input():
    return """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".split()

def test_solve(input):
    x =solve(input)
    
    assert len(x)==41

def test_solve2(input):
    assert solve2(input)==6

def test_initial_position(input):
    assert find_start(input)==(6,4)
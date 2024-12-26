from pytest import fixture
from solve import solve
from solve2 import solve as solve2


@fixture
def simple_input():
    return """
..90..9
...1.98
...2..7
6543456
765.987
876....
987....""".split()

@fixture
def input():
    return """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split()

@fixture
def input2():
    return """"
..90..9
...1.98
...2..7
6543456
765.987
876....
987....""".split()

def test_solve1_0(simple_input):
    x = solve(simple_input)
    assert x==4

def test_solve1_2(input):
    x = solve(input)
    assert x==36

def test_solve2_0(input2):
    x = solve2(input2)
    assert x==13
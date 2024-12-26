from pytest import fixture
from solve import solve
# from solve2 import solve as solve2


@fixture
def intput():
    return """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".split()

def test_solve(intput):
    assert solve(intput)==1930

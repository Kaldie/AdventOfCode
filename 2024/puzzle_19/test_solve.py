from pytest import fixture
from solve import solve
# from solve2 import solve as solve2


@fixture
def intput():
    return """""".split("\n")

def test_solve(intput):
    assert solve(intput,12)==22

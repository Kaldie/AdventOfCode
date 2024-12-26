from pytest import fixture
from solve2 import solve
# from solve2 import solve as solve2


@fixture
def intput():
    return """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE""".split()

def test_solve(intput):
    assert solve(intput)==236

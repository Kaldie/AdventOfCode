from pytest import fixture
from solve import solve
from solve2 import solve as solve2


@fixture
def simple_input():
    return ["""125 17""".strip()]

def test_solve(simple_input):
    assert solve(simple_input,3)==5
    assert solve(simple_input,4)==9
    assert solve(simple_input,5)==13
    assert solve(simple_input,6)==22
    assert solve(simple_input,25)==55312

def test_repetitive_pattern():
    x = set()
    for i in range(30):
        for a in solve2(["0"],i)[1]:
            x.add(a)
            print(len(x))
    assert False
from pytest import fixture
from solve import Machine, _solve, solve
# from solve2 import solve as solve2


@fixture
def intput():
    return """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""".split("\n")

def test_solve(intput):
    assert solve(intput)=="4,6,3,5,6,3,5,2,1,0"

def test_a():
    machine= Machine(0, 0, 9, 0,[2,6])
    _solve(machine)
    assert machine.regB==1

    machine= Machine(10, 0, 0, 0,[5,0,5,1,5,4])
    _solve(machine)
    assert machine.output==[0, 1, 2]


    machine= Machine(2024, 0, 0, 0,[0,1,5,4,3,0])
    _solve(machine)
    assert machine.output==[4,2,5,6,7,7,7,7,3,1,0]
    assert machine.regA==0

    machine= Machine(0, 29, 0, 0,[1,7])
    _solve(machine)
    assert machine.regB==26

    machine= Machine(0, 2024, 43690, 0,[4,0])
    _solve(machine)
    assert machine.regB==44354
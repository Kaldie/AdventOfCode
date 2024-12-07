from pytest import fixture
from solve import solve
from solve2 import solve as solve2

@fixture
def test_input():
    return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

@fixture
def test_input_2():
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

@fixture
def test_input2():
    return "mul(498,303);when()}!(%mul(846,233)-"

def test_solve(test_input):
    assert solve([test_input]) ==  161

def test_solve2(test_input2):
    print(498*303)
    assert solve([test_input2]) == 498*303 + 846*233

def test_solve2_1(test_input_2):
    assert solve2([test_input_2]) ==  48

def test_solve2_2(test_input2):
    print(498*303)
    assert solve2([test_input2]) == 498*303 + 846*233


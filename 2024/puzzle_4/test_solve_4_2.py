from pytest import fixture
from solve2 import search_from_index, solve


@fixture
def test_input():
    return """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".split()


@fixture
def test_input2():
    return """
..X...
.SAMX.
.A..A.
XMAS.S
.X....
""".split()


def test_solve(test_input: str):
    assert solve(test_input) == 9

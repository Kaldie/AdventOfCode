from pytest import fixture
from solve import search_from_index, solve


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
    assert solve(test_input) == 18


def test_solve2(test_input2: str):
    assert search_from_index(needle="XMAS", lines=test_input2, index=(0, 2)) == 1
    assert solve(test_input2) == 4


def test_specific2(test_input2: str):
    index = (4, 1)
    assert search_from_index(needle="XMAS", lines=test_input2, index=index) == 1


def test_specific(test_input: str):
    index = (len(test_input) - 1, len(test_input[0]) - 1)
    assert search_from_index(needle="XMAS", lines=test_input, index=index) == 2

    index = (len(test_input) - 1, len(test_input[0]) - 5)
    assert search_from_index(needle="XMAS", lines=test_input, index=index) == 3

    index = (4, 0)
    assert search_from_index(needle="XMAS", lines=test_input, index=index) == 1

    index = (1, 4)
    assert search_from_index(needle="XMAS", lines=test_input, index=index) == 1

    index = (0, 4)
    assert search_from_index(needle="XMAS", lines=test_input, index=index) == 1

    index = (3, len(test_input[0]) - 1)
    assert search_from_index(needle="XMAS", lines=test_input, index=index) == 2

    index = (5, 6)
    assert search_from_index(needle="XMAS", lines=test_input, index=index) == 1

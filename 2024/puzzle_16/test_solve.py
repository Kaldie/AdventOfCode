from pytest import fixture
from solve import get_score_increase, solve
# from solve2 import solve as solve2


@fixture
def intput():
    return """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".split()

def test_solve(intput):
    assert solve(intput)==7036


def test_get_score_increase():
    assert get_score_increase((0,1),(0,1))==1
    assert get_score_increase((0,1),(0,-1))==2001
    assert get_score_increase((0,1),(1,0))==1001, "get_score_increase((0,1),(1,0))"
    assert get_score_increase((0,1),(-1,0))==1001
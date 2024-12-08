from pytest import fixture
from solve import solve, find_node
from solve2 import solve as solve2


@fixture
def input():
    return """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".split()

def test_solve(input):
    x =solve(input)
    new_lines=[]
    for i,line in enumerate(input):
        new_line=""
        for j in range(len(line)):
            cur = (i,j)
            if cur in x:
                new_line+="#"
            else:
                new_line+=line[j]
        new_lines.append(new_line)

    for a in new_lines:
        print(a)
    print(x)
    assert len(x)==14

def test_solve2(input):
    x =solve2(input)
    new_lines=[]
    for i,line in enumerate(input):
        new_line=""
        for j in range(len(line)):
            cur = (i,j)
            if cur in x:
                new_line+="#"
            else:
                new_line+=line[j]
        new_lines.append(new_line)

    for a in new_lines:
        print(a)
    print(x)
    assert len(x)==34


def test_find_node():
    assert find_node((3,4),(5,5)) == (1,3)
    assert find_node((5,5),(3,4)) == (7,6)
from dataclasses import dataclass
from functools import cache
import math
import pathlib


@cache
def center_given_size(size):
    print(size, math.floor(size / 2))
    return math.floor(size / 2)


def is_on_edge(position, size):
    # gives if is on edge with treshold
    return center_given_size(size) == position


@dataclass
class Machine:
    x: int | None = None
    y: int | None = None
    vx: int | None = None
    vy: int | None = None


def solve_machine(machine: Machine, size: tuple[int, int]):
    
    # perform tick
    # move
    machine.x += machine.vx * 100
    machine.y += machine.vy* 100

    # wrap
    machine.x = machine.x % size[0]
    machine.y = machine.y % size[1]

    quad = 0
    if is_on_edge(machine.x, size[0]) or is_on_edge(machine.y, size[1]):
        print(machine, "on edge")
        return None

    if machine.x < center_given_size(size[0]):
        quad = 1
    else:
        quad = 2

    if machine.y > center_given_size(size[1]):
        quad += 2

    assert quad != 0, "goofed"
    print(
        machine,
        quad,
    )
    return quad


def yield_machine(lines: list[str]):
    for line in lines:
        machine = Machine()
        p, v = line.strip().split(" ")
        machine.x, machine.y = [int(a) for a in p.split("=")[1].split(",")]
        machine.vx, machine.vy = [int(a) for a in v.split("=")[1].split(",")]
        yield machine


def solve(lines: list[str], size):
    """
    This are the equetions we need to do
    a=(Y-BY/BX*X)/(AY-AX*BY/BX)
    b=(X-a*AX)/BX
    """

    total = [0, 0, 0, 0]
    for x in yield_machine(lines):
        index = solve_machine(x, size)
        if index is not None:
            index -= 1
            total[index] = total[index] + 1

    grand_total = 1
    print(total)
    for x in total:
        grand_total *= x
    return grand_total


if __name__ == "__main__":
    SIZE = (101, 103)
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines, SIZE)))

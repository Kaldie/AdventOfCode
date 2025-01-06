import copy
import math
import pathlib


def solve(lines: list[str]):
    return 0


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines,steps=1024,size=71)))

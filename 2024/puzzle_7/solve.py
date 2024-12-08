import pathlib


def solve(lines: list[str]):
    total = 0
    for line in lines:
        value, opperators = [x.strip() for x in line.split(":")]
        value = int(value)

        opperators = [int(x.strip()) for x in opperators.split()]

        if _solve(value, opperators):
            print(value)
            total += value
    return total


def _solve(value: int, opperators: list[int]):
    current_sums = []
    current_sums.append(opperators.pop(0))

    for opperator in opperators:
        new_sums = []
        for sum in current_sums:
            if sum + opperator <= value:
                new_sums.append(sum + opperator)
            if sum * opperator <= value:
                new_sums.append(sum * opperator)
        current_sums = new_sums

    return any([value == x for x in current_sums])


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = handle.readlines()
        print(solve(lines))

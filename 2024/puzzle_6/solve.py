import pathlib


def find_start(lines: list[str]):
    for line_index, line in enumerate(lines):
        try:
            index = line.index("^")
            return line_index, index
        except ValueError:
            pass

def move_dir_to_right(dir: tuple[int, int]):
    if dir == (-1, 0):
        return (0, 1)
    if dir == (0, 1):
        return (1, 0)
    if dir == (1, 0):
        return (0, -1)
    if dir == (0, -1):
        return (-1, 0)
    raise ValueError("booboo", dir)


def is_out_of_bounds(current, bounds):
    for a, limit in zip(current, bounds):
        if a >= limit:
            return True
        if a < 0:
            return True
    return False


def solve(lines: list[str]):
    hight, width = (len(lines), len(lines[0].strip()))
    direction = (-1,0)
    current_index = find_start(lines)
    places = set([current_index])
    while True:
        next_position = tuple([a + b for a, b in zip(current_index, direction)])
        
        if is_out_of_bounds(next_position, (hight, width)):
            break

        if lines[next_position[0]][next_position[1]] == "#":
            direction = move_dir_to_right(direction)
        else:
            current_index = next_position
            places.add(current_index)

    return places


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = handle.readlines()
        print(len(solve(lines)))

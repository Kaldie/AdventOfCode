import copy
import math
import pathlib


def find_element(lines: list[str], element: str):
    positions = []
    for i, line in enumerate(lines):
        index = -1
        while True:
            try:
                index = line[index + 1 :].index(element) + index + 1
                positions.append((i, index))
            except:
                break
    return positions


def get_score_increase(cur_dir, next_dir):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cur_index = dirs.index(cur_dir)
    next_index = dirs.index(next_dir)
    score = 1

    left_turns = 0
    right_turns = 0

    left_index = copy.copy(cur_index)
    right_index = copy.copy(cur_index)

    while not (left_index == next_index) and not (right_index == next_index):
        left_index = left_index + 1 if left_index + 1 < len(dirs) else 0
        left_turns += 1

        right_index = right_index - 1 if right_index - 1 >= 0 else 3
        right_turns += 1

    return score + min(right_turns, left_turns) * 1000


def solve(lines: list[str]):

    start = find_element(lines, "S")
    print(start)
    assert len(start) == 1
    start = start[0]

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    solutions = []  # score + list of lists with paths
    front_locations = [(start, 0, (0, 1), [start])]
    seen_locations = {start: 0}
    i = 0
    min_score = math.inf

    while True:
        i += 1
        new_front = []
        for location, value, cur_dir, path in front_locations:
            for direction in dirs:
                next_step = (location[0] + direction[0], location[1] + direction[1])
                next_char = lines[next_step[0]][next_step[1]]
                new_score = value + get_score_increase(cur_dir, direction)
                
                if new_score > min_score:
                    print("new_score > min_score")
                    continue

                if next_char == "E":
                    if new_score <= min_score:
                        min_score=new_score
                        solutions.append((new_score, [path + [next_step]]))

                elif next_char == ".":
                    if (
                        next_step in path
                    ):
                        continue

                    new_front.append(
                        (
                            next_step,
                            new_score,
                            direction,
                            path + [next_step],
                        )
                    )

                    seen_locations[next_step] = new_score

        # print("####################################################")
        # for front in new_front:
        #     print(front[1],front[3])

        if len(new_front) == 0:
            break

        front_locations = copy.copy(new_front)

    print("here")
    best_locations = set()
    for x in solutions:
        print(x)
    
    # for x in seen_locations.items():
    #     print(x)

    min_score = min([x[0] for x in solutions])
    for solution in solutions:
        if solution[0] != min_score:
            continue
        for path_in_solution in solution[1]:
            print(path_in_solution)
            for position in path_in_solution:
                best_locations.add(position)

    return len(best_locations)


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines)))

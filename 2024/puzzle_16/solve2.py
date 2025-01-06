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

    assert len(start) == 1
    start = start[0]

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    options = [(start, 0, (0, 1), [start])] 
    min_score = 135536
    solutions = []
    seen={}
    i=0

    while len(options) > 0:
        # print(options)
        # print("len options: ", len(options))
        option = options.pop()

        if option[1] > min_score:
            continue

        if i % 10000==0:
            print(len(options), option[0])
        
        i+=1

        next_steps = [(option[0][0] + dir[0], option[0][1] + dir[1]) for dir in dirs]
        next_chars = [lines[x][y] for x, y in next_steps]

        for next_step, next_char, next_dir in zip(next_steps, next_chars, dirs):

            if next_char == "#":
                continue

            if next_step in option[3]:
                continue

            new_score = option[1] + get_score_increase(option[2], next_dir)

            if new_score > min_score:
                continue

            if next_step in seen:
                if (seen[next_step] + 2000)<  new_score:
                    continue

            if next_char == "E":
                min_score = min(min_score, new_score)
                solutions.append((new_score, option[3] + [next_step]))

            elif next_char == ".":
                options.append(
                    (next_step, new_score, next_dir, option[3] + [next_step])
                )
                seen[next_step]=new_score

    best_locations = set()
    min_score = min([x[0] for x in solutions])
    for solution in solutions:
        if solution[0] > min_score:
            continue

        print(solution, "\n")
        for position in solution[1]:
            best_locations.add(position)

    return len(best_locations)


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines)))

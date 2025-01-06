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

    while not(left_index == next_index) and  not(right_index == next_index):
        left_index = left_index + 1 if left_index + 1 < len(dirs) else 0
        left_turns += 1

        right_index = right_index - 1 if right_index -1 >= 0 else 3
        right_turns += 1


    return score + min(right_turns, left_turns) * 1000


def solve(lines: list[str]):

    start = find_element(lines, "S")
    print(start)
    assert len(start) == 1
    start = start[0]

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cur_min = math.inf
    front_locations = {start: (0, (0, 1))}
    seen_locations = {start:0}
    i=0
    while True:
        i+=1
        new_front = {}
        for location, (value, cur_dir) in front_locations.items():
            for direction in dirs:
                next_step = (location[0] + direction[0], location[1] + direction[1])
                next_char = lines[next_step[0]][next_step[1]]
                if next_char == "E":
                    print("found solution: ", value + get_score_increase(cur_dir, direction), i3,,)
                    cur_min = min(
                        [cur_min, value + get_score_increase(cur_dir, direction)]
                    )
                elif next_char == ".":
                    new_score = value + get_score_increase(cur_dir, direction)
                    if next_step in seen_locations and seen_locations[next_step] < new_score:
                        continue
               
                    new_front[next_step] = (
                        new_score,
                        direction,
                    )
                    
                    seen_locations[next_step] = new_score

        if len(new_front) == 0:
            break
        
        # if i >= 5:
        front_locations=copy.copy(new_front)
    print(i)

    return cur_min


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines)))

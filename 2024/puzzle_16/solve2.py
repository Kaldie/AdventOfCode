import pathlib


def find_walls(lines: list[str]):
    walls = find_chars(lines, "#",double=True)
    # unpack
    return [wall for wallx in walls for wall in wallx]


def find_boxes(lines: list[str]):
    return find_chars(lines, "O", double=True)


def find_robot(lines: list[str]):
    robots = find_chars(lines, "@",double=False)
    assert len(robots) == 1
    return robots[0]


def find_chars(lines: list[str], char: str, double: bool = False):
    elements: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for i, line in enumerate(lines):
        for j, v in enumerate(line):
            if v == char:
                if double:
                    elements.append(((i, j * 2), (i, j * 2 + 1)))
                else:
                    elements.append((i, j * 2))

    return elements


def print_state(robot, boxes, walls):
    max_cor = max([wall[0] for wall in walls]), max([wall[1] for wall in walls])

    for i in range(max_cor[0] + 1):
        line = ""
        for j in range( max_cor[1] + 1):
            if (i, j) == robot:
                line += "@"
            elif (i, j) in walls:
                line += "#"
            elif ((i, j), (i, j + 1)) in boxes:
                line += "[]"
            elif ((i, j-1), (i, j)) in boxes:
                continue
            else:
                line += "."
        print(line)
    print()


def move_robot(
    char: str,
    robot: tuple[int, int],
    boxes: list[tuple[int, int]],
    walls: list[tuple[int, int]],
):
    if char == "^":
        dir = [-1, 0]
    if char == ">":
        dir = [0, 1]
    if char == "v":
        dir = [1, 0]
    if char == "<":
        dir = [0, -1]

    boxes_to_move = set()
    new_positions = [robot]
    run_into_wall = False

    unpacked_boxes = [box for boxx in boxes for box in boxx]

    while len(new_positions) > 0:
        # untill we find a wall or an open spot
        positions_to_check = [
            (position_to_check[0] + dir[0], position_to_check[1] + dir[1])
            for position_to_check in new_positions
        ]

        new_positions = set()

        for position_to_check in positions_to_check:
            if position_to_check in walls:
                run_into_wall = True
                new_positions = []  # force we break out of while
                break
            elif position_to_check in unpacked_boxes:
                for index, box_pair in enumerate(boxes):
                    if position_to_check in box_pair:
                        boxes_to_move.add(index)

                        for index, box in enumerate(box_pair):
                            box_dir=(box[0]+dir[0], box[1]+dir[1])
                            box_index = 1 if index==0 else 0
                            if box_dir != box_pair[box_index]:
                                new_positions.add(box)

    if not run_into_wall:
        robot = (robot[0] + dir[0], robot[1] + dir[1])
        for box_index in boxes_to_move:
            box = boxes[box_index]
            boxes[box_index] = (
                (box[0][0] + dir[0], box[0][1] + dir[1]),
                (box[1][0] + dir[0], box[1][1] + dir[1]),
            )

    return robot


def solve(lines: list[str]):
    for index, line in enumerate(lines):
        if len(line.strip()) == 0:
            split = index
            break

    walls = find_walls(lines[:split])
    boxes = find_boxes(lines[:split])
    robot = find_robot(lines[:split])

    for line in lines[split:]:
        for char in line:
            robot=move_robot(char,robot,boxes,walls)

    total = 0
    for box,_ in boxes:
        total += 100 * box[0] + box[1]

    return total


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = [line.strip() for line in handle.readlines()]
        print((solve(lines)))

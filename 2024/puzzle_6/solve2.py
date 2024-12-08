import copy
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


def is_loop(lines: list[str]):
    hight, width = (len(lines), len(lines[0].strip()))
    direction = (-1,0)
    current_index = find_start(lines)
    places = set([(current_index,direction)])
    while True:
        next_position = tuple([a + b for a, b in zip(current_index, direction)])
        
        if is_out_of_bounds(next_position, (hight, width)):
            break

        if lines[next_position[0]][next_position[1]] == "#":
            direction = move_dir_to_right(direction)
        else:
            current_index = next_position
            
            if (current_index,direction) in places:
                return True
            
            places.add((current_index,direction))

    return False

def adjust_lines(lines, location):
    new_lines = copy.copy(lines)
    line = new_lines[location[0]]
    line = line[:location[1]] + "#" + line[location[1]+1:]
    new_lines[location[0]]=line
    return new_lines

def solve(lines):
    total=0
    start = find_start(lines)
    current_line_index=0
    for line_index,line in enumerate(lines):
        for column_index in range(len(line)):
            
            if current_line_index != line_index:
                current_line_index = line_index
                print(line_index)

            if start == (line_index,column_index):
                continue

            new_lines = adjust_lines(lines,(line_index,column_index))
            if is_loop(lines=new_lines):
                total+=1
    return total

if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as handle:
        lines = handle.readlines()
        print(solve(lines))
